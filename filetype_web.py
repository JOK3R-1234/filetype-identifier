#!/usr/bin/env python3
from flask import Flask, render_template, request, session
from pathlib import Path
import binascii, mimetypes, string, tempfile
from datetime import datetime

app = Flask(__name__)
app.secret_key = "supersecretkey"
app.config['MAX_CONTENT_LENGTH'] = 100*1024*1024  # 100MB

# File signatures
SIGNATURES = {
    "PDF":[{"hex":"25504446","offset":0}],
    "PNG":[{"hex":"89504E47","offset":0}],
    "JPEG":[{"hex":"FFD8FF","offset":0}],
    "GIF":[{"hex":"47494638","offset":0}],
    "ZIP":[{"hex":"504B0304","offset":0}],
    "GZIP":[{"hex":"1F8B08","offset":0}],
    "MP3":[{"hex":"494433","offset":0}],
    "MP4":[{"hex":"66747970","offset":4}],
    "ELF":[{"hex":"7F454C46","offset":0}],
    "EXE":[{"hex":"4D5A","offset":0}],
}

# Utilities
def bytes_to_hex(b): return binascii.hexlify(b).upper().decode()
def read_bytes(path,length=66000):
    with open(path,"rb") as f: return f.read(length)
def is_text_file(sample:bytes):
    if not sample or b'\x00' in sample: return False
    text_chars=bytes(string.printable,"utf-8")
    printable_count=sum(1 for b in sample if b in text_chars)
    return printable_count/len(sample)>0.95
def match_signature(blob):
    hex_blob=bytes_to_hex(blob)
    for ftype,sigs in SIGNATURES.items():
        for sig in sigs:
            sig_hex=sig["hex"].upper()
            offset=sig.get("offset",0)
            start=offset*2; end=start+len(sig_hex)
            if end<=len(hex_blob) and hex_blob[start:end]==sig_hex:
                return ftype,sig_hex,offset
    return None

class IdentificationResult:
    def __init__(self,file_type,confidence,details=None):
        self.file_type=file_type
        self.confidence=confidence
        self.details=details or {}

def identify_file(path:Path):
    if not path.exists(): return IdentificationResult("File not found","None",{"path":str(path)})
    blob=read_bytes(path)
    sig_result=match_signature(blob)
    if sig_result:
        ftype,sig_hex,offset=sig_result
        return IdentificationResult(ftype,"High",{"method":"magic signature","signature":sig_hex,"offset":offset})
    sample=blob[:4096]
    if is_text_file(sample):
        mt,_=mimetypes.guess_type(path.name)
        subtype=mt if mt and mt.startswith("text/") else "text/plain"
        return IdentificationResult("TEXT","High (heuristic)",{"method":"text heuristic","mimetype_guess":subtype})
    ext=path.suffix.lower().lstrip(".")
    if ext: return IdentificationResult(f"Unknown (.{ext})","Low (extension only)",{"method":"extension","extension":ext})
    return IdentificationResult("Unknown","Low",{"method":"no match"})

# Routes
@app.route("/",methods=["GET","POST"])
def analyze():
    if "history" not in session: session["history"]=[]
    results=[]
    if request.method=="POST":
        uploaded_files=request.files.getlist("file")
        for f in uploaded_files:
            temp_path=Path(tempfile.gettempdir())/f.filename
            f.save(temp_path)
            try: r=identify_file(temp_path)
            finally: temp_path.unlink()
            conf_class="high" if r.confidence.startswith("High") else "medium" if r.confidence.startswith("Medium") else "low"
            res_dict={"filename":f.filename,"file_type":r.file_type,"confidence":r.confidence,
                      "details":r.details,"confidence_class":conf_class,
                      "timestamp":datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
            results.append(res_dict)
            session["history"].insert(0,res_dict); session.modified=True
    return render_template("analyze.html", results=results, active='analyze', history=session.get("history",[]))

@app.route("/history")
def history():
    hist=session.get("history",[])
    return render_template("history.html", history=hist, active='history')

@app.route("/about")
def about():
    return render_template("about.html", active='about')

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)

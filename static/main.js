document.addEventListener("DOMContentLoaded",function(){
    // Drag-drop
    let dz=document.getElementById('dropzone');
    if(dz){
        dz.addEventListener('dragover',e=>{e.preventDefault(); dz.classList.add('dragover');});
        dz.addEventListener('dragleave',e=>{dz.classList.remove('dragover');});
        dz.addEventListener('drop',e=>{e.preventDefault(); dz.classList.remove('dragover'); document.getElementById('fileinput').files=e.dataTransfer.files;});
    }

    // Falling texts
    const types=['PDF','MP3','MP4','TXT','DOCX','PNG','JPEG','GZIP','EXE','ELF'];
    function createFallingText(){
        for(let i=0;i<50;i++){
            let span=document.createElement('span');
            span.classList.add('falling-text');
            span.style.left=Math.random()*100+'vw';
            span.style.top=Math.random()*100+'vh';
            span.style.fontSize=12+Math.random()*25+'px';
            span.style.opacity=(0.2+Math.random()*0.5).toString();
            span.innerText=types[Math.floor(Math.random()*types.length)];
            document.body.appendChild(span);
            fall(span, Math.random()*2+1);
        }
    }
    function fall(el,speed){
        function step(){
            let top=parseFloat(el.style.top.replace('px',''))+speed;
            if(top>window.innerHeight){ top=-50; el.style.left=Math.random()*100+'vw'; }
            el.style.top=top+'px';
            requestAnimationFrame(step);
        }
        requestAnimationFrame(step);
    }
    createFallingText();
});

// Theme toggle
function toggleTheme(){
    document.body.classList.toggle('light');
    document.querySelectorAll('table.table-result').forEach(t=>t.classList.toggle('light-mode'));
}

// Copy buttons
function copyText(row){
    let txt='';
    row.querySelectorAll('td').forEach(td=>{txt+=td.innerText.replace(/\n/g,' ')+'\t';});
    navigator.clipboard.writeText(txt.trim());
}
function copyAll(){
    let txt='';
    document.querySelectorAll('.table-result tbody tr').forEach(row=>{
        row.querySelectorAll('td').forEach(td=>{txt+=td.innerText.replace(/\n/g,' ')+'\t';});
        txt+='\n';
    });
    navigator.clipboard.writeText(txt.trim());
}

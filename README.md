# File Type Identifier - Web Version

A **professional, web-based file type identification tool** built with Python and Flask. Detects file types accurately using **magic signatures, text heuristics, and extensions**, and presents results in a visually appealing, interactive interface.

---

## Features

- Detects all common file types (PNG, JPG, MP3, MP4, PDF, DOCX, GZ, TAR, WAV, OGG, ISO, TXT, Python scripts, and more).  
- **High-confidence detection** for both binary and text files.   
- **Dark/Light mode toggle** with smooth transitions.  
- **Copy buttons** beside each result and option to copy all results at once.  
- **History table**: sortable, expandable, and color-coded by confidence.  
- Responsive design for desktops, tablets, and mobile devices.  
- Interactive animations for buttons, headers, and table highlights.  

---

## Requirements

- Python 3.8+  
- Pip 3  
- Flask (and other dependencies in `requirements.txt`)

---

## Installation & Usage

1. Clone the repository:

```bash
git clone https://github.com/username/filetype-identifier.git
cd filetype-identifier/
```

2. Install dependencies:

```bash
pip3 install -r requirements.txt
```

3. Run the web app:

```bash
./run.sh
```

4. Open your browser at:

```text
http://127.0.0.1:5000
```

---

## Directory Structure

```text
web/
├── filetype_web.py          # Flask backend
├── static/
│   ├── main.js              # JavaScript
│   └── style.css            # CSS
├── templates/
│   ├── base.html            # Base template
│   ├── analyze.html         # Analyze tab
│   ├── history.html         # History tab
│   └── about.html           # About tab
├── run.sh                   # Easy launch script
├── requirements.txt         # Python dependencies
└── README.md                # Project description
```

---

## About / How it Works

The File Type Identifier detects file types using a **combination of three methods**:

1. **Magic Signature Detection**: Checks the file’s binary signature (first few bytes) for known patterns.  
2. **Text Heuristics**: Determines if a file is plain text (Python, TXT, Markdown, etc.) based on content analysis.  
3. **Extension Fallback**: Uses the file extension when other methods cannot confidently detect the type.  

The tool is designed to provide **fast, accurate, and visually clear results** via a modern web interface.  
It includes a **history table**, **copy functionality**, and a **dark/light theme toggle** for professional usability.

---

## License

MIT License – free to use, modify, and distribute.

---

## Optional Enhancements / Future Features

- Export analysis results as CSV/JSON for reporting.  
- Bulk file uploads with drag-and-drop support.  
- Real-time progress indicators for large files.  
- GitHub badges for Python version, license, stars, forks, etc.  
- Screenshots or GIFs for web interface preview.

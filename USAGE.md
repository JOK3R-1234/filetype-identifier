# File Type Identifier - Web Version Usage

This guide explains how to use the **File Type Identifier Web Tool** built with Python and Flask.

**Prerequisites:**  
- Python 3.8 or higher installed  
- Pip 3  
- All dependencies listed in `requirements.txt`

---

## Installation and Setup

1. **Clone the repository** to your local machine:  
   `git clone https://github.com/username/filetype-identifier.git`  
   Navigate to the web folder:  
   `cd filetype-identifier/web`

2. **Install required dependencies:**  
   `pip3 install -r requirements.txt`

3. **Run the web application:**  
   `./run.sh`

4. **Open your web browser** and go to:  
   `http://127.0.0.1:5000`

---

## Using the Tool

- Navigate to the **Analyze** tab.  
- Upload files by clicking the upload area or drag-and-drop your files.  
- The tool will automatically detect each file type and display results along with confidence levels.  
- Use the **Copy** button beside each file to copy individual results, or use the **Copy All** button to copy all results at once.  
- Switch between **Dark and Light mode** using the theme toggle in the interface.

---

## Viewing History

- Go to the **History** tab to see all previously analyzed files.  
- The table is **sortable** and **color-coded by confidence level**.  
- Click any row to expand and view detailed results.

---

## Stopping the Server

- Once finished, stop the web server in your terminal using `Ctrl+C`.  
- Temporary files are automatically cleaned up on exit.

---

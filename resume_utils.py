import docx2txt
import fitz  # PyMuPDF

def extract_text_from_pdf(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    text = "\n".join([page.get_text() for page in doc])
    return text

def extract_text_from_docx(file):
    return docx2txt.process(file)

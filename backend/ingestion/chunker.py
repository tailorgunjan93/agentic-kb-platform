import fitz
import docx
import os

def chunk_text(text,chunk_size=5000):
    return [text[i:i+chunk_size] for i in range(0,len(text),chunk_size)]

def chunk_pdf(file_path,chunk_size=5000):
    """
    Extracts text from a PDF file and splits it into fixed-size chunks.

    Args:
        file_path (str): Path to the PDF file.
        chunk_size (int): Number of characters per chunk.

    Returns:
        List[str]: List of text chunks.
    """

    doc = fitz.open(file_path) #Load Pdf
    full_text = "".join([page.get_text() for page in doc]) # Concatenate all page text    
    return chunk_text(full_text,chunk_size)

def chunk_doc(file_path,chunk_size=500):
    doc = docx.open(file_path)
    text = "\n".join([p.text for p in doc.paragraphs])
    return chunk_text(text,chunk_size)

def chunk_txt(file_path,chunk_size=500):
    with open(file_path,'r',encoding="utf-8") as f:
        full_text = f.read()
    return chunk_txt(full_text,chunk_size)

def chunk_files(file_path,chunk_size=5000):
    ext = os.path.splitext(file_path)[1].lower()
    if ext==".pdf":
       return chunk_pdf(file_path,chunk_size)
    elif ext==".docx":
        return chunk_doc(file_path,chunk_size)
    elif ext==".txt":
        return chunk_txt(file_path,chunk_size)
    else:
        raise ValueError(f"Unsupported file type {ext} for file {file_path}")

        

import os

def get_pdf_path():
    
    pdf_path = input("Please enter the path to your PDF file (e.g., data/your_file.pdf): ").strip()
    
    
    if os.path.isfile(pdf_path):
        print(f"PDF path set to: {pdf_path}")
        return pdf_path
    else:
        print(f"PDF file not found at the specified path: {pdf_path}")
        return None


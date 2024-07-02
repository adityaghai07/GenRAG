
pdf_path = 'data/The_intelligent_investor.pdf'

import fitz 
from tqdm.auto import tqdm 

def text_formatter(text: str) -> str:

    cleaned_text = text.replace("\n", " ").strip() 
    return cleaned_text


def open_and_read_pdf(pdf_path: str) -> list[dict]:

    print(f"Opening and reading PDF: {pdf_path}")
    doc = fitz.open(pdf_path) 
    pages_and_texts = []
    for page_number, page in tqdm(enumerate(doc)):  
        text = page.get_text()  
        text = text_formatter(text)
        pages_and_texts.append({"page_number": page_number - 41, 
                                "page_char_count": len(text),
                                "page_word_count": len(text.split(" ")),
                                "page_sentence_count_raw": len(text.split(". ")),
                                "page_token_count": len(text) / 4,  
                                "text": text})
        
    print(f"Total pages: {len(pages_and_texts)}")
    return pages_and_texts



# testing
# pages_and_texts = open_and_read_pdf(pdf_path=pdf_path)
# print(pages_and_texts[:15])
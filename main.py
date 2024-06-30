from services.pdf_to_text import open_and_read_pdf,text_formatter
from tqdm.auto import tqdm
from services.text_to_chucks import split_list
import pandas as pd
import random
from spacy.lang.en import English 
nlp = English()
nlp.add_pipe("sentencizer")

pdf_path = 'data/The_intelligent_investor.pdf'
num_sentence_chunk_size = 10

pages_and_texts = open_and_read_pdf(pdf_path=pdf_path)

for item in tqdm(pages_and_texts):
    item["sentences"] = list(nlp(item["text"]).sents)

    item["sentences"] = [str(sentence) for sentence in item["sentences"]]
     
    item["page_sentence_count_spacy"] = len(item["sentences"])


for item in tqdm(pages_and_texts):
    item["sentence_chunks"] = split_list(input_list=item["sentences"],
                                         slice_size=num_sentence_chunk_size)
    item["num_chunks"] = len(item["sentence_chunks"])


df = pd.DataFrame(pages_and_texts)
print(df.describe().round(2))
print(df.head(5))
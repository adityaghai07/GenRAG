from services.pdf_to_text import open_and_read_pdf,text_formatter
from tqdm.auto import tqdm
from services.text_to_chucks import split_list
from services.process_chunks import process_chunks
from services.embed_model import embed_text
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


# df = pd.DataFrame(pages_and_texts)
# print(df.describe().round(2))
# print(df.head(5))

pages_and_chunks = process_chunks(pages_and_texts=pages_and_texts)

df = pd.DataFrame(pages_and_chunks)
print(df.describe().round(2))

min_token_length = 30
# for row in df[df["chunk_token_count"] <= min_token_length].sample(5).iterrows():
 
#     print(f'Chunk token count: {row[1]["chunk_token_count"]} | Text: {row[1]["sentence_chunk"]}')

pages_and_chunks_over_min_token_len = df[df["chunk_token_count"] > min_token_length].to_dict(orient="records")
# pages_and_chunks_over_min_token_len[:2]



embed_text(pages_and_chunks_over_min_token_len)

print(pages_and_chunks_over_min_token_len[0])


print("Saving text chunks and embeddings to CSV")

text_chunks_and_embeddings_df = pd.DataFrame(pages_and_chunks_over_min_token_len)
embeddings_df_save_path = "data/text_chunks_and_embeddings_df.csv"
text_chunks_and_embeddings_df.to_csv(embeddings_df_save_path, index=False)



text_chunks_and_embedding_df_load = pd.read_csv(embeddings_df_save_path)
print(text_chunks_and_embedding_df_load.head())
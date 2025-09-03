from sentence_transformers import SentenceTransformer
from tqdm.auto import tqdm
import pandas as pd
import numpy as np
import torch
from time import sleep
from services.retrieve import print_wrapped,retrieve_relevant_resources,print_top_results_and_scores
from llm.get_response import ask


device = "cpu"
query = input("Enter your query: ")



print("The device is set to:",device)
print("This may take a while...")

sleep(2)


print("Loading the Saved Embeddings DataFrame...")

embeddings_df_save_path = "data/text_chunks_and_embeddings_df.csv"
text_chunks_and_embeddings_df = pd.read_csv(embeddings_df_save_path)




print("Converting the 'embedding' column to a numpy array...")
sleep(2)


pages_and_chunks = text_chunks_and_embeddings_df.to_dict(orient="records")

embeddings_list = text_chunks_and_embeddings_df['embedding']
cleaned_embeddings = []

for embedding in embeddings_list:
    embedding_cleaned = embedding.replace('tensor([', '').replace('])', '')
    embedding_array = np.array([float(i) for i in embedding_cleaned.split(',')])
    cleaned_embeddings.append(embedding_array)

embeddings_matrix = np.vstack(cleaned_embeddings)
embeddings = torch.tensor(embeddings_matrix, dtype=torch.float32)

print("Embeddings tensor (768, N):", embeddings)
print("Shape of embeddings:", embeddings.shape)



print("Successsfully Converted the 'embedding' column to a torch tensor.")
sleep(2)

print("\n\n")
print("Retrieving the most relevant resources...")
print("\n\n")

sleep(2)


print_top_results_and_scores(query=query, embeddings=embeddings, pages_and_chunks=pages_and_chunks)

 
print("Using Gemini to generate a response...")
print("\n\n")
sleep(2)




ans = ask(query=query, embeddings=embeddings, pages_and_chunks=pages_and_chunks,embeddings_df_save_path=embeddings_df_save_path)

print_wrapped(ans)

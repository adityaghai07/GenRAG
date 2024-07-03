from sentence_transformers import SentenceTransformer
from tqdm.auto import tqdm
import pandas as pd
import numpy as np
import torch
from services.retrieve import print_wrapped,retrieve_relevant_resources,print_top_results_and_scores
from llm.get_response import ask


device = "cpu"
query = input("Enter your query: ")
# query = "What is the best way to invest in the stock market?"


print("The device is set to:",device)
print("This may take a while...")


print("Loading the Saved Embeddings DataFrame...")

embeddings_df_save_path = "data/text_chunks_and_embeddings_df.csv"
text_chunks_and_embeddings_df = pd.read_csv(embeddings_df_save_path)




print("Converting the 'embedding' column to a numpy array...")
text_chunks_and_embeddings_df["embedding"] = text_chunks_and_embeddings_df["embedding"].apply(lambda x: np.fromstring(x.strip("[]"), sep=" "))


pages_and_chunks = text_chunks_and_embeddings_df.to_dict(orient="records")
embeddings = torch.tensor(np.array(text_chunks_and_embeddings_df["embedding"].tolist()), dtype=torch.float32).to(device)

print("Successsfully Converted the 'embedding' column to a torch tensor.")


print("\n\n")
print("Retrieving the most relevant resources...")
print("\n\n")
print("Using Gemini to generate a response...")
print("\n\n")

ans = ask(query=query, embeddings=embeddings, pages_and_chunks=pages_and_chunks,embeddings_df_save_path=embeddings_df_save_path)

print_wrapped(ans)










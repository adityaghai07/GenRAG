from sentence_transformers import SentenceTransformer
from tqdm.auto import tqdm
import pandas as pd
import numpy as np
import torch
from services.retrieve import print_wrapped,retrieve_relevant_resources,print_top_results_and_scores

# device = "cuda" if torch.cuda.is_available() else "cpu"
device = "cpu"

# Load the embeddings
embeddings_df_save_path = "data/text_chunks_and_embeddings_df.csv"
text_chunks_and_embeddings_df = pd.read_csv(embeddings_df_save_path)

text_chunks_and_embeddings_df["embedding"] = text_chunks_and_embeddings_df["embedding"].apply(lambda x: np.fromstring(x.strip("[]"), sep=" "))

pages_and_chunks = text_chunks_and_embeddings_df.to_dict(orient="records")

embeddings = torch.tensor(np.array(text_chunks_and_embeddings_df["embedding"].tolist()), dtype=torch.float32).to(device)



query = "What is the best way to invest in the stock market?"

scores, indices = retrieve_relevant_resources(query=query,
                                              embeddings=embeddings)
print(scores, indices)

print_top_results_and_scores(query=query,
                             embeddings=embeddings,pages_and_chunks=pages_and_chunks)




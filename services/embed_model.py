from sentence_transformers import SentenceTransformer
from tqdm.auto import tqdm
import torch

# device = "cuda" if torch.cuda.is_available() else "cpu"
device = "cpu"

print(f"Loading the model on device: {device}")
embedding_model = SentenceTransformer(model_name_or_path="all-mpnet-base-v2", 
                                      device=device)

embedding_model.to(device)

print("Model loaded successfully")

def embed_text(pages_and_chunks_over_min_token_len):

    print("Embedding text chunks")
    for item in tqdm(pages_and_chunks_over_min_token_len):
        item["embedding"] = embedding_model.encode(item["sentence_chunk"])

    

    



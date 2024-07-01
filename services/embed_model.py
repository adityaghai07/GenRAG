from sentence_transformers import SentenceTransformer
from tqdm.auto import tqdm
import torch

# device = "cuda" if torch.cuda.is_available() else "cpu"
device = "cpu"

embedding_model = SentenceTransformer(model_name_or_path="all-mpnet-base-v2", 
                                      device=device)

embedding_model.to(device)

def embed_text(pages_and_chunks_over_min_token_len):

    for item in tqdm(pages_and_chunks_over_min_token_len):
        item["embedding"] = embedding_model.encode(item["sentence_chunk"])

    # text_chunks = [item["sentence_chunk"] for item in pages_and_chunks_over_min_token_len]

    # text_chunk_embeddings = embedding_model.encode(text_chunks,
    #                                            batch_size=32, # you can use different batch sizes here for speed/performance, I found 32 works well for this use case
    #                                            convert_to_tensor=True) # optional to return embeddings as tensor instead of array
    

    



# from llm.llm_response import llm_response
from llm.get_gemini_response import get_gemini_response
from services.retrieve import retrieve_relevant_resources

def ask (query, embeddings, pages_and_chunks,embeddings_df_save_path,):
    """
    Takes a query, retrieves most relevant resources and prints them out in descending order.

    Note: Requires pages_and_chunks to be formatted in a specific way (see above for reference).
    """
    
    scores, indices = retrieve_relevant_resources(query=query,
                                                  embeddings=embeddings)
    

    
    context_items = [pages_and_chunks[i] for i in indices]

# Extract the 'content' from each dictionary and join them into a single string
    context = "- " + "\n- ".join([item["sentence_chunk"] for item in context_items])


    for i, item in enumerate(context_items):
        item["score"] = scores[i].cpu()

    print(f"query: {query}")
    print("\n\n")

    ans = get_gemini_response(query=query,context=context)

    return ans
    

    
    
    
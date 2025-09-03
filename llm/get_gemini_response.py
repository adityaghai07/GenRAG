from google import genai
import os
import dotenv

dotenv.load_dotenv()
client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash-lite", contents="Explain how AI works in a few words"
)


def get_gemini_response(context, query):

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"""
    Using the context given below answer the query.
                                    
    CONTEXT: {context}

    QUERY: {query}
    """)

    return response.text



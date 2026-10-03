from dotenv import load_dotenv
from groq import Groq
import os
from src.search import context ,query


load_dotenv()

client=Groq(api_key=os.getenv("GROQ_API_KEY"))
def get_answer(question,context):


    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
        {
        "role":"user",
        "content":f"""
         use this context below to answer the question

         Context:
         {context}

         Question:
         {query}

        """
        }
    ]
)

response=get_answer(query,context)


print(response)



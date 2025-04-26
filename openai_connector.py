import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def ask_openai(user_query):
    response = openai.chat.completions.create(
        model=os.getenv("OPENAI_DEPLOYMENT_NAME"),
        messages=[
            {"role": "user", "content": user_query}
        ],
        temperature=0.7,
        max_tokens=1000,
        top_p=0.9,
        frequency_penalty=0.2,
        presence_penalty=0.3
    )
    return response.choices[0].message.content

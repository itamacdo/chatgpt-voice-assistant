from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def perguntar_chatgpt(pergunta):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": pergunta}
        ]
    )
    return response.choices[0].message.content

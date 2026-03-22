import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_draft(facts: str):
    prompt = f"""
    You are a federal civil litigator.

    Facts:
    {facts}

    Draft a persuasive legal argument.
    """

    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content

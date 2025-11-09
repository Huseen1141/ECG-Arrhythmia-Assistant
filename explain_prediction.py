import os
from openai import OpenAI
from dotenv import load_dotenv

# Load the API key from .env file
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def explain_prediction(label: str) -> str:
    prompt = f"""I am building a medical assistant that explains ECG arrhythmia types in simple terms.

Explain what "{label}" means in a short and friendly way (for someone who doesn’t know medicine)."""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=150
    )

    return response.choices[0].message.content

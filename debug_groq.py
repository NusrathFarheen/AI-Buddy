import os
from dotenv import load_dotenv
from groq import Groq

# Manually load .env from root
load_dotenv(".env")

key = os.getenv("GROQ_API_KEY")
print(f"Key loaded: {key[:5]}...{key[-5:] if key else 'None'}")

client = Groq(api_key=key)

try:
    print("Sending request to Groq...")
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "Say hello"
            }
        ],
        model="llama-3.3-70b-versatile",
    )
    print("Success!")
    print(chat_completion.choices[0].message.content)
except Exception as e:
    print(f"ERROR: {e}")

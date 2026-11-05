import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = os.getenv("GEMINI_MODEL")

try:

    response = client.models.generate_content(
        model=model,
        contents="Reply with: AI Support Desk is working!"
    )

    print("Gemini API connection successful!")
    print(response.text)

except Exception as error:

    print("Gemini API connection failed!")
    print(error)
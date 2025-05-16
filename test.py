from dotenv import load_dotenv, find_dotenv
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
print(f"API Key: {api_key}")

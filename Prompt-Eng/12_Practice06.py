import os 
from google import genai
from dotenv import load_dotenv

load_dotenv()

client=genai.Client()

prompt = """
    Explain embeddings in exactly three bullet points, using simple English and no more than 50 words.

    Return a JSON object with keys 'title', 'difficulty', and 'language' for a beginner Python tutorial. Return valid JSON only.
"""

response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents=prompt
)
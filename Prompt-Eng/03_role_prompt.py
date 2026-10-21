import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client();

prompt = """
Act as an experienced Python tutor.

Explain Python lists to a beginner.
Use simple English and include one code example.
Keep the answer under 100 words.
"""

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=prompt
)

print(response.text)
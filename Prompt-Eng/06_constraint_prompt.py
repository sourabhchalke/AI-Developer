import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client()

prompt = """
Explain prompt engineering.

Constraints:
- Use exactly 3 bullet points.
- Use simple English.
- Maximum 50 words.
- Do not include an introduction.
- Return only the bullet points.
"""

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=prompt
)

print(response.text);

import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client()

prompt = """
    Task:
Rewrite the following message as a professional email.

Message:
"hey sir i need two days leave for family work"

Instructions:
1. Add a subject line.
2. Use a polite greeting.
3. Explain the leave request clearly.
4. End with a professional closing.
"""

response = client.models.generate_content(model="gemini-3.8-flash", contents=prompt)

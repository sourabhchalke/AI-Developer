import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client()

prompt="""
Context:
I am a beginner building an AI Content Assistant
using React, Node.js, Express, and Gemini.

Task:
Explain how my application sends a prompt
to Gemini and displays the generated response.

Use a simple step-by-step explanation.
"""

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=prompt
)
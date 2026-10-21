import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client=genai.Client()

prompt="""
    Compare zero-shot and few-shot prompting. Include a definition, one example of each, and a final comparison.

    Generate five beginner interview questions about REST APIs and provide a short answer to each.
"""

response=client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents=prompt
)

print(response.text)
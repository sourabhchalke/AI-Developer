import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client()


# Context prompting examples
prompt="""
    Context: I am a beginner building an AI Content Assistant with React, Node.js, Express, and Gemini. Explain the flow from a button click to the generated response.

    Context: I have 30 minutes a day to study LLMs. Create a realistic one-week learning plan with a small coding task each day.

    Context: My audience is non-technical HR recruiters. Explain what an LLM API does without assuming programming knowledge.
"""

response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents=prompt
)

print(response.text);
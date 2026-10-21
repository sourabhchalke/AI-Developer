# Zero-Shot Prompting

import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client()

# Zero-Shot Prompting Examples
prompt="""
    Zero-Shot Translate 'I am learning artificial intelligence' into Marathi. Return only the translation.

    Zero-Shot Summarize this sentence in one sentence: 'LLMs generate text based on patterns learned from large amounts of training data.'

    Extract the programming languages from: 'I use Python, JavaScript, and Java, but I am currently learning Python.' Return a JSON array of unique languages.
"""

response=client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents=prompt
)
print(response.text);

import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client()

# Role prompting examples
prompt="""
    Act as a Python tutor. Explain lists to a beginner using one example and under 80 words.

    Act as a senior MERN developer. Explain the purpose of Express.js routes and show a short example.

    Act as a technical interviewer. Ask me five beginner-level JavaScript questions, one at a time.

    Act as a code reviewer. Review a short Python function for readability and possible bugs. Explain your suggestions.
"""

response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents=prompt
)

print(response.text)
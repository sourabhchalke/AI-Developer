import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client=genai.Client()

# Few Shot prompting examples
prompt="""
    Teach the model a sentiment-labeling pattern using three examples, then classify: 'The service was amazing.'

    Provide two examples of converting informal messages into professional messages, then convert: 'hey send me the file asap'.

    Demonstrate converting a task into a priority label using two examples, then classify: 'Production server is down.' Use High, Medium, or Low.

    Give two examples of formatting names as 'Last name, First name', then format: 'Aarav Sharma'.
"""

res = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents=prompt
)

print(res.text);
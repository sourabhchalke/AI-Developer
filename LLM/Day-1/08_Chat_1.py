#Based on above topics

import os,tiktoken
from dotenv import load_dotenv
from google import genai
from google.genai import types


load_dotenv()
client=genai.Client(api_key=os.getenv("GEMINIAI_API_KEY"))

userInput=input("Enter your question : ")

MODEL = "gemini-3.8-flash"
SYSTEM = "You are a Python tutor. Max 30 words."
USER = userInput
TEMPERATURE=0.3

#tokens
enc=tiktoken.get_encoding("cl100k_base")
print("input tokens :",len(enc.encode(SYSTEM+USER)))

#call
r=client.models.generate_content(
    model=MODEL,
    contents=USER,
    config=types.GenerateContentConfig(
        system_instruction=SYSTEM,
        temperature=TEMPERATURE,
    ),
)

#response
print(r.text)

#Usage
if r.usage_metadata:
    print("Prompt Tokens : ",r.usage_metadata.prompt_token_count)
    print("Output Tokens : ",r.usage_metadata.candidates_token_count)
    print("Total Tokens : ",r.usage_metadata.total_token_count)
    # print("Usage metadata:", r.usage_metadata)
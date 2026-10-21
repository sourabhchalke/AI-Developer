
import os
from dotenv import load_dotenv
from google import genai

# 1. Load variables from the .env file into the environment
load_dotenv()

# 2. Initialize the client. 
# It will automatically look for the GEMINI_API_KEY environment variable.
client = genai.Client()

prompt = """
Classify customer reviews as Positive or Negative.

Review: "Amazing quality and excellent service."
Answer: Positive

Review: "The product broke after one day."
Answer: Negative

Review: "I love this product."
Answer:
"""

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=prompt
)

print(response.text)

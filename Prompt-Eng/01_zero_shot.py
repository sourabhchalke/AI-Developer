
import os
from dotenv import load_dotenv
from google import genai

# 1. Load variables from the .env file into the environment
load_dotenv()

# 2. Initialize the client. 
# It will automatically look for the GEMINI_API_KEY environment variable.
client = genai.Client()

prompt = """
Classify this review as Positive, Negative, or Neutral.

Review: "The product is excellent, but delivery was late."

Return only the classification.
"""

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=prompt
)

print(response.text)

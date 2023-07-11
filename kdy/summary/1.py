import os
import openai
from dotenv import load_dotenv


load_dotenv()
api_key = os.environ.get("api_key")

openai.api_key = api_key

response = openai.Completion.create(
  engine="text-davinci-002",
  prompt="Translate the following English text to French: '{}'",
  max_tokens=60
)

print(response.choices[0].text.strip())

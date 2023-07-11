import os
import openai
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("api_key")
openai.organization = "org-F7T21Cs6VigBP2jR3VGzwbgZ"
openai.api_key = api_key
openai.Model.list()
print(openai.api_key)
print(openai.Model.list())

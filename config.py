# config.py
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

# Retrieve the API key and verify it's loaded correctly
api_key = os.getenv('OPENAI_API_KEY')
if not api_key:
    raise EnvironmentError("OPENAI_API_KEY environment variable not set. Please check your .env file.")

# Initialize the OpenAI client with the API key
openai = OpenAI(api_key=api_key)

# Model specification
MODEL = "gpt-4o-mini"

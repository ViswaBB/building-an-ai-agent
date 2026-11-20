import os
from dotenv import load_dotenv
from openai import OpenAI
import argparse

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")

args = parser.parse_args()

messages = [
    {"role": "user", "content": args.user_prompt}
]

response = client.chat.completions.create(
    model="openrouter/free",
    messages=messages
)

if args.verbose:
    print("User prompt:", args.user_prompt)
    print("Prompt tokens:", response.usage.prompt_tokens)
    print("Response tokens:", response.usage.completion_tokens)
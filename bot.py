from importlib.metadata import version

print(version("typing_extensions"))


from openai import OpenAI
import openai
from config import settings


client = OpenAI(api_key = settings.openai_api_key)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

print(completion)


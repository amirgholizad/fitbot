from openai import OpenAI
from fastapi import FastAPI, Form
from typing import Annotated
from config import settings

client = OpenAI(api_key = settings.openai_api_key)

chat_log = []
system_message = {"role": "system",
      "content": "You are a helpful assistant named Jarvis"}
chat_log.append(system_message)

app = FastAPI()

@app.post("/fitbot")
async def fitbot(user_input: Annotated[str, Form()]):

  chat_log.append({"role": "user", "content": user_input})
  response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=chat_log,
    temperature=0.6
  )

  bot_response = response.choices[0].message.content
  chat_log.append({"role": "assistant", "content": bot_response})
  return bot_response

from openai import OpenAI
from fastapi import FastAPI, Form, Request
from typing import Annotated
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from config import settings

client = OpenAI(api_key = settings.openai_api_key)

chat_log = []
chat_responses = []
system_message = {"role": "system",
      "content": "You are a helpful assistant named Jarvis"}
chat_log.append(system_message)

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def chat_page(request: Request):
  return templates.TemplateResponse("bot.html", {"request": request})

@app.post("/", response_class=HTMLResponse)
async def chat(request: Request, user_input: Annotated[str, Form()]):
  chat_log.append({"role": "user", "content": user_input})
  chat_responses.append(user_input)
  response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=chat_log,
    temperature=0.6
  )

  bot_response = response.choices[0].message.content
  chat_log.append({"role": "assistant", "content": bot_response})
  chat_responses.append(bot_response)
  return templates.TemplateResponse("bot.html", {"request": request, "chat_responses": chat_responses})

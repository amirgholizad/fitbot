from openai import OpenAI
from fastapi import FastAPI, Form, Request, WebSocket
from typing import Annotated
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from config import settings

client = OpenAI(api_key = settings.openai_api_key)

data:str = open("data.txt", "r").read()
chat_log = []
chat_responses = []
system_message = {"role": "system",
      "content": "You are a fitness advisor named Jarvis. Use these data as a reference for tricep exercises: f{data}"}
chat_log.append(system_message)

app = FastAPI()
templates = Jinja2Templates(directory="templates")
static = app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def chat_page(request: Request):
  return templates.TemplateResponse("bot.html", {"request": request})


@app.websocket("/ws")
async def chat(websocket: WebSocket):
  await websocket.accept()
  while True:
    user_input = await websocket.receive_text()
    chat_log.append({"role": "user", "content": user_input})
    chat_responses.append(user_input)

    try:
      response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=chat_log,
        temperature=0.6,
        stream=True
      )

      ai_response = ''

      for chunk in response:
        if chunk.choices[0].delta.content is not None:
          ai_response += chunk.choices[0].delta.content
          await websocket.send_text(chunk.choices[0].delta.content)
      chat_responses.append(ai_response)

    except Exception as e:
      await websocket.send_text(f"Error: {str(e)}")
      break 

# @app.post("/", response_class=HTMLResponse)
# async def chat(request: Request, user_input: Annotated[str, Form()]):
#   chat_log.append({"role": "user", "content": user_input})
#   chat_responses.append(user_input)
#   response = client.chat.completions.create(
#     model="gpt-3.5-turbo",
#     messages=chat_log,
#     temperature=0.6
#   )

#   bot_response = response.choices[0].message.content
#   chat_log.append({"role": "assistant", "content": bot_response})
#   chat_responses.append(bot_response)
#   return templates.TemplateResponse("bot.html", {"request": request, "chat_responses": chat_responses})
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from uvicorn import run
import html

app = FastAPI()

@app.get("/", response_class=PlainTextResponse)
def greet(name: str = "Юзернейм", message: str = "Давай дружить"):
    safe_name = html.escape(name)
    safe_message = html.escape(message)
    return f"Hello {safe_name}! {safe_message}!"
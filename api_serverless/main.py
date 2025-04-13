from fastapi import FastAPI, Request
from mangum import Mangum
from suggest import generate_suggestion

app = FastAPI()

@app.post("/suggestion")
async def get_suggestion(request: Request):
    body = await request.json()
    user_message = body.get("user_message", "")
    suggestion = generate_suggestion(user_message)
    return {"suggestion": suggestion}

handler = Mangum(app)
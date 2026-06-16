from fastapi import FastAPI
from .routers.users import router

app = FastAPI()


@app.get("/")
def health_check():
    return {"status": "ok"}

app.include_router(router)
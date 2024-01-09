from fastapi import FastAPI
from api import router
from db import Base, engine


Base.metadata.create_all(bind=engine)


app = FastAPI()

app.include_router(router)


@app.get("/")
async def root():
    return {"message": "Hello World"}

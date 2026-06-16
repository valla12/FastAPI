import tables
import uvicorn
from fastapi import FastAPI
from database import engine
from routers import post, user, auth

tables.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)


@app.get("/")
def root():
    return {"hello": 'fastapi'}


# This is exactly what Flask does under the hood!
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
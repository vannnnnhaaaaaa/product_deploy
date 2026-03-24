from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

print('hello')

# Cho phép Frontend gọi API
app.add_middleware(CORSMiddleware, allow_origins=["*"])

@app.get("/api/tasks")
def get_tasks():
    return [{"id": 1, "title": "Học Docker"}, {"id": 2, "title": "Deploy VPS"}]


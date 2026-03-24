from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

# Cho phép Frontend gọi API
app.add_middleware(CORSMiddleware, allow_origins=["*"])

@app.get("/api/tasks")
def get_tasks():
    # Giữ lại dòng code mới nhất có tên bạn
    return [{"id": 1, "title": "Học Docker"}, {"id": 2, "title": "Deploy VPS"}, {"status": "Docker is awesome", "user": "Văn Hà"}]
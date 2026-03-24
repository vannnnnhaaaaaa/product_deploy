from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

<<<<<<< Updated upstream
=======
print('hello')
print('hello 2')

>>>>>>> Stashed changes
# Cho phép Frontend gọi API
app.add_middleware(CORSMiddleware, allow_origins=["*"])

@app.get("/api/tasks")
def get_tasks():
<<<<<<< Updated upstream
    return [{"id": 1, "title": "Học Docker"}, {"id": 2, "title": "Deploy VPS"}]
=======
    return [{"id": 1, "title": "Học Docker"}, {"id": 2, "title": "Deploy VPS"},{"status": "Docker is awesome", "user": "Văn Hà"}]

>>>>>>> Stashed changes

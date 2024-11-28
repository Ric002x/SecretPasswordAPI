import uvicorn

from app.main import app
from app.schedule_words import start_schedule

if __name__ == "__main__":
    start_schedule()
    uvicorn.run(app, host='0.0.0.0', port=8000)

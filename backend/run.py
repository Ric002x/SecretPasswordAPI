import uvicorn

from app import create_api
from app.schedule_words import start_schedule

api = create_api()

if __name__ == "__main__":
    start_schedule()
    uvicorn.run(api, host='0.0.0.0', port=8080)

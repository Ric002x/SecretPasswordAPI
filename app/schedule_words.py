import random as rd
import threading
import time
from datetime import datetime
from zoneinfo import ZoneInfo
from .database import Words, session_db


def get_random_word():
    with open("app/dictionary.txt", 'r') as file:
        words = file.read().split('\n')
        random_word = rd.choice(words)
        return random_word


def schedule_job():
    while True:
        timezone = ZoneInfo("America/Fortaleza")
        now = datetime.now(timezone)
        if now.hour == 12 and now.minute == 0:
            word = get_random_word()
            existing_word = session_db.query(
                Words).filter_by(word=word).first()

            if not existing_word:
                save_word = Words(
                    word=word
                )
                session_db.add(save_word)
                session_db.commit()

            if session_db.query(Words).count() > 10:
                oldest_word = session_db.query(
                    Words).order_by(Words.id.desc()).first()
                session_db.delete(oldest_word)
                session_db.commit()

            time.sleep(60)
        time.sleep(1)


def start_schedule():
    scheduler_thread = threading.Thread(target=schedule_job)
    scheduler_thread.daemon = True
    scheduler_thread.start()

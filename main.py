from collections import Counter

import uvicorn
from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from database import Words, session_db
from schedule_words import start_schedule

with open("./dictionary.txt", 'r') as file:
    ALL_WORDS = set(file.read().splitlines())


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5500",  # BackEnd
                   "http://127.0.0.1:5500"],  # FrontEnd
    allow_credentials=True,
)


@app.get('/current-word')
def get_today_word():
    last_word = session_db.query(Words).order_by(Words.id.desc()).first()
    if not last_word:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error getting today's word"
        )
    return JSONResponse({"word": last_word.word})


@app.get('/validate/{word}')
def validate_word(word: str):
    if word not in ALL_WORDS or len(word) != 5:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            detail=f"The word {word.upper()} doesn't exist"
        )
    return JSONResponse(
        {"message": f"the word {word.upper()} is valid"}
    )


@app.get("/check-word/{word}")
def validate_word_guess(word: str):
    last_word_object = session_db.query(
        Words).order_by(Words.id.desc()).first()
    if not last_word_object:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error getting today's word"
        )
    today_word = last_word_object.word

    if word == today_word:
        return JSONResponse({
            "status": "correct",
            "validation": [2 for _ in range(5)]
        })

    else:
        word_letters_validation = [0 for _ in range(5)]
        letters_counter = Counter(today_word)

        for i in range(len(word)):
            if word[i] == today_word[i]:
                word_letters_validation[i] = 2
                letters_counter[word[i]] -= 1

        for i in range(len(word)):
            if word[i] in today_word \
                and letters_counter[word[i]] > 0 \
                    and word_letters_validation[i] == 0:
                word_letters_validation[i] = 1
                letters_counter[word[i]] -= 1

    return JSONResponse(
        {
            "status": "incorrect",
            "validation": word_letters_validation,
        }
    )


if __name__ == "__main__":
    start_schedule()
    uvicorn.run(app, host='0.0.0.0', port=8000)

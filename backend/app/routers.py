from collections import Counter

from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse

from .database import Words, session_db

with open("app/dictionary.txt", 'r') as file:
    ALL_WORDS = set(file.read().splitlines())

router = APIRouter()


@router.get('/current-word')
async def get_today_word():
    last_word = session_db.query(Words).order_by(Words.id.desc()).first()
    if not last_word:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error getting today's word"
        )
    return JSONResponse({"word": last_word.word})


@router.get('/validate/{word}')
async def validate_word(word: str):
    if word not in ALL_WORDS or len(word) != 5:
        return {"validate": False}
    return JSONResponse(
        {"validate": True}
    )


@router.get("/check-word/{word}")
async def validate_word_guess(word: str):
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

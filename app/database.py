from sqlalchemy import String, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column

engine = create_engine("sqlite:///./words.db", echo=True)

session_db = Session(engine)


class Base(DeclarativeBase):
    pass


class Words(Base):
    __tablename__ = "game_words"

    id: Mapped[int] = mapped_column(primary_key=True)
    word: Mapped[str] = mapped_column(String(5))

    def __init__(self, word):
        self.word = word

    def __repr__(self) -> dict:
        return {
            'id': self.id,
            'word': self.word
        }


Base.metadata.create_all(engine)
if not session_db.query(Words).all():
    first_word = Words(
        word="mundo"
    )
    session_db.add(first_word)
    session_db.commit()

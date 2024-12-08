from sqlalchemy import String, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker

from .config import settings

engine = create_engine(
    settings.DATABASE_URL, connect_args=settings.DATABASE_CONNECT_DICT
)
session_db = sessionmaker(autocommit=False, autoflush=False, bind=engine)()


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

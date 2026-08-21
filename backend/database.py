from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from configs.env import env
from typing import Generator

engine = create_engine(env.database_url)

SessionLocal = sessionmaker(bind=engine, autoflush=False)

Base = declarative_base()


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db() -> None:
    Base.metadata.create_all(bind=engine)

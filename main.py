from fastapi import FastAPI
from collections import Counter
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

postgresengine = create_engine("postgresql://postgres:5526678@localhost/postgres")

PostgresSession = sessionmaker(bind=postgresengine)
app = FastAPI()

Base = declarative_base()


class Devices(Base):
    __tablename__ = 'devices'

    id = Column(Integer, primary_key=True)
    dev_id = Column(String)
    dev_type = Column(String)


def sanitize(text):
    yield from (ch.lower() for ch in text.lower() if ch.isalpha())


@app.get("/")
def verify_anagrams(first='aaa', second='bbb'):
    counter = Counter(sanitize(first)) == Counter(sanitize(second))
    if counter == True:
        return {"Слово является анаграммой"}
    else:
        return {"Слово не является анаграммой"}


if __name__ == '__main__':
    verify_anagrams()
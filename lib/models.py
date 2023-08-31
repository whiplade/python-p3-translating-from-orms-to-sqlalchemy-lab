#!/usr/bin/env python3

from sqlalchemy import Column, String, Integer, create_engine, PrimaryKeyConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Dog(Base):
    __tablename__ = "dogs"

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    breed = Column(String())

    def repr(self) -> str:
        return f"Dog {self.id}: " + f"{self.name}, " + f"Breed {self.breed}"


if __name__ == "main":
    SQLITE_URL = "sqlite:///dogs.db"
    engine = create_engine(SQLITE_URL)
    Base.metadata.create_all(engine)
    # Using our engine to configure a "Session" class
    Session = sessionmaker(bind=engine)

    # Using "Session" class to create "session" object
    session = Session()
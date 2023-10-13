from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from . import crud
from . import models
from . import schemas

from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/hello")
def read_root() -> dict:
    return {"Nachricht": "Ich lieb dich",
            "Nachricht2": "Hallo, ich bin ReST",
            "Nachricht3": "Hallo, ich bin ein Pi"}


@app.post("/new_value")
def create_value(temp_id: int, item: schemas.Temperatures, db: Session = Depends(get_db)):
    return crud.create_reading(db=db, temperature=item), temp_id

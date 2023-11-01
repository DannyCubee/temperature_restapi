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


@app.post("/api/v1/new-temperature")
def create_value(item: schemas.CreateTemp, db: Session = Depends(get_db)):
    return crud.create_reading(db, item)


@app.get("/api/v1/temperatures/{id}", response_model=schemas.Temperatures)
def get_value(id: int, db: Session = Depends(get_db)):
    return crud.get_reading(db, id)


@app.put("/api/v1/update")
def update_value(id: int, temp_c: int, temp_f: int, db: Session = Depends(get_db)):
    return crud.update_reading(db, id, temp_c, temp_f)


@app.delete("/api/v1/delete")
def delete_value(id: int, db: Session = Depends(get_db)):
    return crud.delete_reading(db, id)


@app.get("/api/v1/all-items")
def get_all_values(skip: int, limit: int, db: Session = Depends(get_db)):
    return crud.get_all_readngs(db, skip, limit)


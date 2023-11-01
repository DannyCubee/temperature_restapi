from sqlalchemy.orm import Session, Query
from sqlalchemy import select, update

from . import models
from . import schemas


def create_reading(db: Session, temperature: schemas.Temperatures):
    new_temp = models.Temperature(**temperature.model_dump())
    db.add(new_temp)
    db.commit()
    db.refresh(new_temp)
    return new_temp


def get_reading(db: Session, lookup_id: int):
    temp_reading = db.query(models.Temperature).filter(models.Temperature.id == lookup_id).first()
    return temp_reading


def update_reading(db: Session, id: int, new_temp_c, new_temp_f):
    db.query(models.Temperature).where(models.Temperature.id == id).\
        update({"temp_c": new_temp_c, "temp_f": new_temp_f}, synchronize_session='evaluate')

    db.commit()

    return db.query(models.Temperature).where(models.Temperature.id == id).first()


def delete_reading(db: Session, id: int):
    db.query(models.Temperature).filter(models.Temperature.id == id).\
        delete(synchronize_session=False)

    db.commit()

    return {"msg": f"Dataset with ID:{id} deleted"}

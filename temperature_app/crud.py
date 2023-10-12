from sqlalchemy.orm import Session

from . import models
from . import schemas


def create_reading(db: Session, temperature: schemas.Temperatures, id:int):
    new_temp = models.Temperature(id=int)
    db.add(new_temp)
    db.commit()
    db.refresh(new_temp)
    return new_temp

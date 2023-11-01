from sqlalchemy import Boolean, Column, Integer, Float

from .database import Base


class Temperature(Base):
    __tablename__ = "temperatures"

    id = Column(Integer, primary_key=True, autoincrement=True)
    temp_c = Column(Float)
    temp_f = Column(Float)

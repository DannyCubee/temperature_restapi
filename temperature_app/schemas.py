from pydantic import BaseModel


class Temperatures(BaseModel):
    temp_c: float
    temp_f: float


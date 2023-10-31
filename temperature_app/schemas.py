from pydantic import BaseModel


class Temperatures(BaseModel):
    id: int
    temp_c: float
    temp_f: float


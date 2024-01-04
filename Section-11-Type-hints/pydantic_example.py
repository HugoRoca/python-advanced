# see pydantic docs
from pydantic import BaseModel, EmailStr, StrictStr, ValidationError
from typing import Optional


class PersonSchema(BaseModel):
    name: StrictStr
    lastname: StrictStr
    phone: int
    email: Optional[EmailStr] = None


try:
    p1 = PersonSchema(name=123, lastname="Roca", phone="1222")

    print(p1)
except ValidationError as e:
    print(e.json())

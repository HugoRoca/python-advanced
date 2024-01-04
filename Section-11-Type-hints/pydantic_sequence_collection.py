from pydantic import BaseModel, StrictStr
from typing import Sequence, Dict, Any, Set


class Generic(BaseModel):
    sequence: Sequence = None
    collection: Set = None


print(
    Generic(sequence=[1,2,3,4]).sequence,
    Generic(sequence=(1,4,6,0)).sequence,
    Generic(collection=[1,2,3,4]).collection
)
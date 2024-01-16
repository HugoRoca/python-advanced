from pydantic import BaseModel, Field, constr, confloat


validate_str = constr(
    max_length=50,
    min_length=3,
    strict=True
)
validate_float = confloat(gt=0.0)


class BaseProduct(BaseModel):
    name: validate_str = Field(...)
    brand: validate_str = Field(...)
    price: validate_float = Field(...)


class Product(BaseProduct):
    id: int = Field(...)

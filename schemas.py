"""Pydantic schemas (request bodies + response models)."""
from pydantic import BaseModel, EmailStr


# ---------- Auth ----------
class UserCreate(BaseModel):
    full_name: str
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    full_name: str
    email: EmailStr

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: UserOut


# ---------- Property ----------
class PropertyBase(BaseModel):
    title: str
    address: str
    city: str
    type: str = "Apartment"
    bedrooms: int = 1
    bathrooms: int = 1
    area_sqft: int = 0
    rent_amount: float = 0
    status: str = "Available"
    tenant_name: str = ""
    description: str = ""
    image_url: str = ""


class PropertyCreate(PropertyBase):
    pass


class PropertyUpdate(PropertyBase):
    pass


class PropertyOut(PropertyBase):
    id: int

    class Config:
        from_attributes = True

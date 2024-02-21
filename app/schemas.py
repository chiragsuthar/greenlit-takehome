from pydantic import BaseModel
from typing import List, Optional

class UserBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    minimum_fee: Optional[int]

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    pass

class User(UserBase):
    id: int

class FilmBase(BaseModel):
    title: str
    description: str
    budget: int
    release_year: int
    genres: List[str]

class FilmCreate(FilmBase):
    pass

class FilmUpdate(FilmBase):
    pass

class Film(FilmBase):
    id: int

class CompanyBase(BaseModel):
    name: str
    contact_email_address: str
    phone_number: str

class CompanyCreate(CompanyBase):
    pass

class CompanyUpdate(CompanyBase):
    pass

class Company(CompanyBase):
    id: int

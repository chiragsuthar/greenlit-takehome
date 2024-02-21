from sqlalchemy.orm import Session

from . import schemas
from . import models

# CRUD operations for users
def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.User).offset(skip).limit(limit).all()

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def update_user(db: Session, user_id: int, user_update: schemas.UserUpdate):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    for key, value in user_update.dict().items():
        setattr(db_user, key, value)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    db.delete(db_user)
    db.commit()

# CRUD operations for films
def create_film(db: Session, film: schemas.FilmCreate):
    db_film = models.Film(**film.dict())
    db.add(db_film)
    db.commit()
    db.refresh(db_film)
    return db_film

def get_films(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Film).offset(skip).limit(limit).all()

def get_film(db: Session, film_id: int):
    return db.query(models.Film).filter(models.Film.id == film_id).first()

def update_film(db: Session, film_id: int, film_update: schemas.FilmUpdate):
    db_film = db.query(models.Film).filter(models.Film.id == film_id).first()
    for key, value in film_update.dict().items():
        setattr(db_film, key, value)
    db.commit()
    db.refresh(db_film)
    return db_film

def delete_film(db: Session, film_id: int):
    db_film = db.query(models.Film).filter(models.Film.id == film_id).first()
    db.delete(db_film)
    db.commit()

# CRUD operations for companies
def create_company(db: Session, company: schemas.CompanyCreate):
    db_company = models.Company(**company.dict())
    db.add(db_company)
    db.commit()
    db.refresh(db_company)
    return db_company

def get_companies(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Company).offset(skip).limit(limit).all()

def get_company(db: Session, company_id: int):
    return db.query(models.Company).filter(models.Company.id == company_id).first()

def update_company(db: Session, company_id: int, company_update: schemas.CompanyUpdate):
    db_company = db.query(models.Company).filter(models.Company.id == company_id).first()
    for key, value in company_update.dict().items():
        setattr(db_company, key, value)
    db.commit()
    db.refresh(db_company)
    return db_company

def delete_company(db: Session, company_id: int):
    db_company = db.query(models.Company).filter(models.Company.id == company_id).first()
    db.delete(db_company)
    db.commit()

# CRUD operations for user's roles with films
def add_user_film_role(db: Session, user_id: int, film_id: int, role: str):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    db_film = db.query(models.Film).filter(models.Film.id == film_id).first()
    if db_user is None or db_film is None:
        return False
    db_user.films.append(db_film)
    db.commit()
    return True

def remove_user_film_role(db: Session, user_id: int, film_id: int):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    db_film = db.query(models.Film).filter(models.Film.id == film_id).first()
    if db_user is None or db_film is None:
        return False
    db_user.films.remove(db_film)
    db.commit()
    return True

# CRUD operations for user's roles with companies
def add_user_company_role(db: Session, user_id: int, company_id: int, role: str):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    db_company = db.query(models.Company).filter(models.Company.id == company_id).first()
    if db_user is None or db_company is None:
        return False
    db_user.companies.append(db_company)
    db.commit()
    return True

def remove_user_company_role(db: Session, user_id: int, company_id: int):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    db_company = db.query(models.Company).filter(models.Company.id == company_id).first()
    if db_user is None or db_company is None:
        return False
    db_user.companies.remove(db_company)
    db.commit()
    return True

from fastapi import FastAPI, HTTPException, Depends, status
from sqlalchemy.orm import Session
from app import crud, models, schemas, database
from app.database import Base, engine

# Create all tables in the database
Base.metadata.create_all(bind=engine)

app = FastAPI()
# Dependency to get the database session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# API endpoints for CRUD operations on users
@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)

@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_users(db=db, skip=skip, limit=limit)

@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return db_user

@app.put("/users/{user_id}", response_model=schemas.User)
def update_user(user_id: int, user_update: schemas.UserUpdate, db: Session = Depends(get_db)):
    db_user = crud.get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return crud.update_user(db=db, user_id=user_id, user_update=user_update)

@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    crud.delete_user(db=db, user_id=user_id)
    return {"message": "User deleted successfully"}

# API endpoints for CRUD operations on films
@app.post("/films/", response_model=schemas.Film)
def create_film(film: schemas.FilmCreate, db: Session = Depends(get_db)):
    return crud.create_film(db=db, film=film)

@app.get("/films/", response_model=list[schemas.Film])
def read_films(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_films(db=db, skip=skip, limit=limit)

@app.get("/films/{film_id}", response_model=schemas.Film)
def read_film(film_id: int, db: Session = Depends(get_db)):
    db_film = crud.get_film(db=db, film_id=film_id)
    if db_film is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Film not found")
    return db_film

@app.put("/films/{film_id}", response_model=schemas.Film)
def update_film(film_id: int, film_update: schemas.FilmUpdate, db: Session = Depends(get_db)):
    db_film = crud.get_film(db=db, film_id=film_id)
    if db_film is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Film not found")
    return crud.update_film(db=db, film_id=film_id, film_update=film_update)

@app.delete("/films/{film_id}")
def delete_film(film_id: int, db: Session = Depends(get_db)):
    db_film = crud.get_film(db=db, film_id=film_id)
    if db_film is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Film not found")
    crud.delete_film(db=db, film_id=film_id)
    return {"message": "Film deleted successfully"}

# API endpoints for CRUD operations on companies
@app.post("/companies/", response_model=schemas.Company)
def create_company(company: schemas.CompanyCreate, db: Session = Depends(get_db)):
    return crud.create_company(db=db, company=company)

@app.get("/companies/", response_model=list[schemas.Company])
def read_companies(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_companies(db=db, skip=skip, limit=limit)

@app.get("/companies/{company_id}", response_model=schemas.Company)
def read_company(company_id: int, db: Session = Depends(get_db)):
    db_company = crud.get_company(db=db, company_id=company_id)
    if db_company is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Company not found")
    return db_company

@app.put("/companies/{company_id}", response_model=schemas.Company)
def update_company(company_id: int, company_update: schemas.CompanyUpdate, db: Session = Depends(get_db)):
    db_company = crud.get_company(db=db, company_id=company_id)
    if db_company is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Company not found")
    return crud.update_company(db=db, company_id=company_id, company_update=company_update)

@app.delete("/companies/{company_id}")
def delete_company(company_id: int, db: Session = Depends(get_db)):
    db_company = crud.get_company(db=db, company_id=company_id)
    if db_company is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Company not found")
    crud.delete_company(db=db, company_id=company_id)
    return {"message": "Company deleted successfully"}

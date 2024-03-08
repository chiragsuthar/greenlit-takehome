from sqlalchemy import Column, Integer, String, ForeignKey, Table, ARRAY
from sqlalchemy.orm import relationship
from .database import Base

# Define the User model
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    minimum_fee = Column(Integer)

    # Define the relationship with films
    films = relationship("Film", secondary="user_film_roles", back_populates="users")
    companies = relationship("Company", secondary="user_company_roles", back_populates="users")

# Define the Film model
class Film(Base):
    __tablename__ = "films"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    budget = Column(Integer)
    release_year = Column(Integer)
    genres = Column(ARRAY(String))

    # Define the relationship with users
    users = relationship("User", secondary="user_film_roles", back_populates="films")

    companies = relationship("Company", secondary="company_film", back_populates="films")

# Define the Company model
class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    contact_email_address = Column(String)
    phone_number = Column(String)

    # Define the relationship with films
    films = relationship("Film", secondary="company_film", back_populates="companies")
    users = relationship("User", secondary="user_company_roles", back_populates="companies")

# Define the join table for user and film roles
user_film_roles = Table(
    "user_film_roles",
    Base.metadata,
    Column("user_id", ForeignKey("users.id"), primary_key=True),
    Column("film_id", ForeignKey("films.id"), primary_key=True),
    Column("role", String),  # "writer", "producer", or "director"
)

# Define the join table for user and company roles
user_company_roles = Table(
    "user_company_roles",
    Base.metadata,
    Column("user_id", ForeignKey("users.id"), primary_key=True),
    Column("company_id", ForeignKey("companies.id"), primary_key=True),
    Column("role", String),  # "owner" or "member"
)

# Define the association table for company and film relationship
company_film = Table(
    "company_film",
    Base.metadata,
    Column("company_id", ForeignKey("companies.id"), primary_key=True),
    Column("film_id", ForeignKey("films.id"), primary_key=True)
)

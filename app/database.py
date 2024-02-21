import urllib.parse

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Encode the username and password
username = "postgres"
password = "postgres"  

encoded_username = urllib.parse.quote_plus(username)
encoded_password = urllib.parse.quote_plus(password)

# SQLAlchemy database URL
SQLALCHEMY_DATABASE_URL = f"postgresql://{encoded_username}:{encoded_password}@localhost:5433/postgres"

# Create the database engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a SessionLocal class to create session objects
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Define the base class for ORM models
Base = declarative_base()

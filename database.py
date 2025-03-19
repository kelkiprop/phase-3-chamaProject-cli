from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


#setting up db connection
DATABASE_URL = "sqlite:///chama.db" 

# Set up SQLAlchemy engine
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)

#define base
Base = declarative_base()

#function to get a new session
def get_session():
    return SessionLocal()

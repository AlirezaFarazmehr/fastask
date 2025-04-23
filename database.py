from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLite database address
SQLALCHEMY_DATABASE_URL = "sqlite:///./tasks.db"

# Create an engine to connect to the database
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Create a session to manage connections
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base classes for defining tables
Base = declarative_base()

# Database model for the tasks table
class TaskModel(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    done = Column(Boolean, default=False)

# Create tables in the database
Base.metadata.create_all(bind=engine)

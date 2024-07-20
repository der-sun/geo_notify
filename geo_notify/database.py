from sqlalchemy import create_engine, Column, Integer, Float, String, Boolean
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker

from config import DATABASE_URL

engine = create_engine(DATABASE_URL, echo=True)
Session = sessionmaker(bind=engine)

class Base(DeclarativeBase): pass

def init_db():
    Base.metadata.create_all(engine)

class PointOfInterest(Base):            ##TODO: add datatime variable for checking in offline mode && history
    __tablename__ = 'pointsofinterest'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    visited = Column(Boolean, default=False)
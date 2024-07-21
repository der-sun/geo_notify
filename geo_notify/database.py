import os
from sqlalchemy import create_engine, Column, Integer, Float, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import DATABASE_URL  # Абсолютный импорт

# Создаем движок SQLAlchemy для работы с базой данных PostgreSQL
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
Base = declarative_base()

# Инициализация базы данных
def init_db():
    Base.metadata.create_all(engine)

# Определяем модель точки интереса
class PointOfInterest(Base):
    __tablename__ = 'pointsofinterest'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    visited = Column(Boolean, default=False)


    ##TODO: add datatime variable for checking in offline mode && history
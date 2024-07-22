# geo_notify/database.py
from sqlalchemy import create_engine, Column, Integer, Float, String, Boolean, BIGINT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import DATABASE_URL

# Создаем базовый класс для всех моделей
Base = declarative_base()

class PointOfInterest(Base):
    __tablename__ = 'points_of_interest'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(BIGINT, nullable=False)
    name = Column(String, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    visited = Column(Boolean, default=False)

# Создаем движок для подключения к базе данных PostgreSQL
engine = create_engine(DATABASE_URL)

# Создаем объект Session для работы с базой данных
Session = sessionmaker(bind=engine)

def init_db():
    # Создаем все таблицы в базе данных
    Base.metadata.create_all(engine)

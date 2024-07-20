from database import init_db, Session, PointOfInterest
#from notifier import check_and_notify
#from telegram_bot import bot

def main():
    init_db()  # Инициализация базы данных
    # Пример: Добавление новой точки интереса
    session = Session()
    new_point = PointOfInterest(name="Example Location", latitude=0.0, longitude=0.0)
    session.add(new_point)
    session.commit()
    print("Точка интереса успешно добавлена!")
    # Логика приложения

if __name__ == '__main__':
    main()

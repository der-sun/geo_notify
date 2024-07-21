from telegram_bot import start_telegram_bot
from database import init_db

def main():
    # Инициализация базы данных
    init_db()
    
    # Запуск Telegram бота
    start_telegram_bot()

if __name__ == '__main__':
    main()

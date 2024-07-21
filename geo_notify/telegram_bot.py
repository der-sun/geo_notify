from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from config import TELEGRAM_API_KEY
from notifier import notify_user_of_points

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Привет! Я GeoNotifyBot. Я помогу тебе отслеживать точки интереса.')

async def add_point_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        name = context.args[0]
        latitude = float(context.args[1])
        longitude = float(context.args[2])
        from logic import add_point
        add_point(name, latitude, longitude)
        await update.message.reply_text(f'Точка интереса "{name}" добавлена.')
    except (IndexError, ValueError):
        await update.message.reply_text('Использование: /addpoint <name> <latitude> <longitude>')

async def check_location_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        user_location = (float(context.args[0]), float(context.args[1]))
        notify_user_of_points(update.message.chat_id, user_location)
        await update.message.reply_text('Проверка завершена.')
    except (IndexError, ValueError):
        await update.message.reply_text('Использование: /checklocation <latitude> <longitude>')

def start_telegram_bot():
    application = ApplicationBuilder().token(TELEGRAM_API_KEY).build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('addpoint', add_point_command))
    application.add_handler(CommandHandler('checklocation', check_location_command))

    application.run_polling()

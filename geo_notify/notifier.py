# notifier.py
from database import Session, PointOfInterest
from geopy.distance import geodesic
import requests
from config import TELEGRAM_API_KEY, RADIUS

def send_telegram_message(chat_id, message):
    url = f"https://api.telegram.org/bot{TELEGRAM_API_KEY}/sendMessage"
    payload = {
        'chat_id': chat_id,
        'text': message
    }
    response = requests.post(url, json=payload)
    return response.json()

def check_in_radius(user_location, point_location, radius):
    user_location = (float(user_location[0]), float(user_location[1]))
    point_location = (float(point_location[0]), float(point_location[1]))
    radius = float(radius)
    return geodesic(user_location, point_location).meters <= radius

def notify_user_of_points(user_id, chat_id, user_location):
    session = Session()
    points = session.query(PointOfInterest).filter(PointOfInterest.user_id == user_id).all()
    for point in points:
        point_location = (point.latitude, point.longitude)
        if check_in_radius(user_location, point_location, RADIUS):
            send_telegram_message(chat_id, f'Вы находитесь в радиусе точки интереса: {point.name}')
            point.visited = True
            session.commit()
    session.close()

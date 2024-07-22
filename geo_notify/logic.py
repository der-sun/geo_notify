# geo_notify/logic.py
from database import Session, PointOfInterest

def add_point(user_id, name, latitude, longitude):
    session = Session()
    point = PointOfInterest(user_id=user_id, name=name, latitude=latitude, longitude=longitude)
    session.add(point)
    session.commit()
    session.close()

def get_points(user_id):
    session = Session()
    points = session.query(PointOfInterest).filter(PointOfInterest.user_id == user_id).all()
    session.close()
    return points

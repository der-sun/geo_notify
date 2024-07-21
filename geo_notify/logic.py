from database import Session, PointOfInterest
from geopy.distance import geodesic

def add_point(name, latitude, longitude):
    session = Session()
    point = PointOfInterest(name=name, latitude=latitude, longitude=longitude)
    session.add(point)
    session.commit()
    session.close()

def check_in_radius(user_location, point_location, radius):
    return geodesic(user_location, point_location).meters <= radius

def mark_point_as_visited(point_id):
    session = Session()
    point = session.query(PointOfInterest).get(point_id)
    point.visited = True
    session.commit()
    session.close()

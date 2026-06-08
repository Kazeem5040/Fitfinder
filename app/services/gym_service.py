import math
import requests

from config import Config


class GymService:
    @staticmethod
    def search_gyms(use_current_location,location, max_distance,latitude,longitude):
        user_latitude = None
        user_longitude = None

        if use_current_location:
            if not latitude or not longitude:
                return []

            user_latitude = float(latitude)
            user_longitude = float(longitude)

        else:
            if not location:
                return []

            coordinates = GymService.get_coordinates_from_location(location)

            if not coordinates:
                return []

            user_latitude = coordinates["latitude"]
            user_longitude = coordinates["longitude"]

        radius_in_meters = max_distance * 1609.34

        places = GymService.get_nearby_gyms(user_latitude,user_longitude,radius_in_meters)

        gyms = []

        for place in places:
            gym_location = place.get("geometry", {}).get("location", {})

            gym_latitude = gym_location.get("lat")
            gym_longitude = gym_location.get("lng")

            if gym_latitude is None or gym_longitude is None:
                continue

            distance = GymService.calculate_distance_in_miles(user_latitude,user_longitude,gym_latitude,gym_longitude)

            if distance <= max_distance:
                gyms.append(
                    {"name": place.get("name", "Unknown Gym"),
                        "address": place.get("vicinity", "Address not available"),
                        "rating": place.get("rating", "N/A"),
                        "distance": round(distance, 2),
                        "price": "N/A"})

        gyms.sort(key=lambda gym: gym["distance"])

        return gyms

    @staticmethod
    def get_coordinates_from_location(location):
        url = "https://maps.googleapis.com/maps/api/geocode/json"

        params = {"address": location, "key": Config.GOOGLE_API_KEY}

        response = requests.get(url, params=params)
        data = response.json()

        if data.get("status") != "OK":
            return None

        first_result = data["results"][0]
        coordinates = first_result["geometry"]["location"]

        return {"latitude": coordinates["lat"],
            "longitude": coordinates["lng"]}

    @staticmethod
    def get_nearby_gyms(latitude, longitude, radius):
        url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"

        params = {"location": f"{latitude},{longitude}",
            "radius": radius,
            "type": "gym",
            "key": Config.GOOGLE_API_KEY}

        response = requests.get(url, params=params)
        data = response.json()

        if data.get("status") not in ["OK", "ZERO_RESULTS"]:
            print("GOOGLE API ERROR:", data)
            return []

        return data.get("results", [])

    @staticmethod
    def calculate_distance_in_miles(user_latitude,user_longitude,gym_latitude,gym_longitude):
        earth_radius_miles = 3958.8
        user_latitude = math.radians(user_latitude)
        user_longitude = math.radians(user_longitude)
        gym_latitude = math.radians(gym_latitude)
        gym_longitude = math.radians(gym_longitude)

        latitude_difference = gym_latitude - user_latitude
        longitude_difference = gym_longitude - user_longitude

        a = (math.sin(latitude_difference / 2) ** 2
            +
            math.cos(user_latitude)
            *
            math.cos(gym_latitude)
            *
            math.sin(longitude_difference / 2) ** 2)

        c = 2 * math.atan2(math.sqrt(a),math.sqrt(1 - a))

        return earth_radius_miles * c
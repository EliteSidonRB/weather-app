from dotenv import load_dotenv
import requests
import os
load_dotenv()

def get_weather(location):

    apikey = os.getenv("API_key")
    url = "http://api.weatherapi.com/v1/current.json"

    params = {
        "key" : apikey,
        "q" : location
    }

    response = requests.get(url, params=params)
    data = response.json()
    city = data["location"]["name"]
    country = data["location"]["country"]
    temp_c = data["current"]["temp_c"]
    temp_f = data["current"]["temp_f"]
    condition_text = data["current"]["condition"]["text"].lower()

    if "sun" in condition_text or "clear" in condition_text:
        condition_class = "sunny"
    elif "rain" in condition_text or "drizzle" in condition_text or "sleet" in condition_text:
        condition_class = "rainy"
    elif "fog" in condition_text or "mist" in condition_text:
        condition_class = "misty"
    elif "snow" in condition_text or "blizzard" in condition_text:
        condition_class = "snowy"
    elif "cloud" in condition_text or "overcast" in condition_text:
        condition_class = "cloudy"
    else:
        condition_class = "default"

    condition_text = condition_text.title()
    return {
        "city" : city,
        "country" : country,
        "temp_c" : temp_c,
        "temp_f" : temp_f,
        "condition" : condition_text,
        "condition_image" : condition_class
    }
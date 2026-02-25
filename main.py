import os
import requests
from twilio.rest import Client


weather_api = os.environ.get("OPENWEATHERMAP_API_KEY")
lati = os.environ.get("LATITUDE")
longi = os.environ.get("LONGITUDE")
my_phone = os.environ.get("MY_PHONE")
sender = os.environ.get("SENDER_PHONE")

# Find your Account SID and Auth Token at twilio.com/console
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")

parameters = {
    "lat": lati,
    "lon": longi,
    "appid": weather_api,
    # "lang": "hi",
    "cnt": 5,             # number of timestamps for near future
}


three_hour_url = "https://api.openweathermap.org/data/2.5/forecast"
response = requests.get(url=three_hour_url,
                        params=parameters)
response.raise_for_status()
results = response.json()
update = "Clear Sky."
for weathers in results["list"]:
    if 500 <= weathers["weather"][0]["id"] < 700:
        update = "It will rain ☔."
    elif weathers["weather"][0]["id"] > 700:
        update = "It's cloudy today."


client = Client(account_sid, auth_token)
try:
    message = client.messages.create(
        body=f"Join Earth's mightiest heroes. Like Kevin Bacon. {update}",
        from_=sender,
        to=my_phone,
    )
    print(f"Message has been sent {message.status}.\n{message.body}")
except Exception as e:
    print(f"Message could not be sent.\n{e}")


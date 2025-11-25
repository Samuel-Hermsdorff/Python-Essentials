import requests
from twilio.rest import Client

api_key = "API_KEY"
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
account_sid = "ACCOUNT_SID"
auth_token = "AUTH_TOKEN"

parameters = {
    "lat": -23.694450,
    "lon": -46.565800,
    "cnt": 4,
    "appid": api_key
}

response = requests.get(url=OWM_Endpoint , params=parameters, timeout=10)
response.raise_for_status()
weather_data = response.json()

# if id < 700: bring an umbrella

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        messaging_service_sid='MGf9fa87b8ceae0c94621b6e8ae39617ab',
        body="It's going to rain today. Remember to bring an ☂️",
        to="+5511934262043"
)
    print(message.status)
weather_description = weather_data["list"][0]["weather"][0]["description"]

print(weather_description)

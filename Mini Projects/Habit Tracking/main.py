import requests
from datetime import datetime

USERNAME = "samuelhermsdorff"
TOKEN = "TOKEN"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params, timeout=10)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Reading Graph",
    "unit": "commit",
    "type": "int",
    "color": "sora" 
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers, timeout=10)
# print(response.text)

pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

today = datetime.now()
# print(today.strftime("%Y%m%d"))

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometers did you cycle today? ")
}

# response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers, timeout=10)
# print(response.text)

update_endpoint = f"{pixel_endpoint}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "1"
}

# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers, timeout=10)
# print(response.text)

# response = requests.delete(url=update_endpoint, headers=headers, timeout=10)

# print(response.text)

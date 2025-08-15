import requests
import os
from dotenv import load_dotenv
from datetime import datetime as dt

load_dotenv()

# OS Environments:
PIXELA_ENDPOINT = os.getenv("PIXELA_ENDPOINT")
API_TOKEN = os.getenv("API_TOKEN")
USER_NAME = os.getenv("USER_NAME")
GRAPH_ID = os.getenv("GRAPH_ID")

# Endpoints:
GRAPH_ENDPOINT = f'{PIXELA_ENDPOINT}/{USER_NAME}/graphs'
GRAPH_ID_ENDPOINT = f"{GRAPH_ENDPOINT}/{GRAPH_ID}"

#Configuration:
create_user_params = {
        "token": API_TOKEN,
        "username": USER_NAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
}

graph_config = {
    "id": GRAPH_ID,
    "name": "Gym Graph",
    "unit": "Day",
    "type": "float",
    "color": "sora",
}

date = dt.now()
today = date.strftime("%Y%m%d")
print(today)

graph_header = {
    "X-USER-TOKEN": API_TOKEN
}

pixel_data = {
    "date": today,
    "quantity": input("How many hours did you workout today?: ")
}

create_once = False
while create_once:
    # Create User:
    create_user_request = requests.post(url=PIXELA_ENDPOINT, json=create_user_params)
    print(create_user_request.text)

    # Create Graph:
    graph_request = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=graph_header)
    print(graph_request.text)

    # Edit Graph:
    graph_edit_request = requests.put(url=GRAPH_ID_ENDPOINT, json={"unit": "Hour(s)"}, headers=graph_header)
    print(graph_edit_request.text)

    create_once = True

# Post a Pixel:
post_pixel = requests.post(url=GRAPH_ID_ENDPOINT, json=pixel_data, headers=graph_header)
print(post_pixel.text)

# Delete a Pixel:
# delete_pixel = requests.delete(url=f'{GRAPH_ID_ENDPOINT}/{today}', headers=graph_header)
# print(delete_pixel.text)



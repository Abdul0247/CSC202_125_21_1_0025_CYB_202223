import requests

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "Wariz"
TOKEN = "mkdmkwdkndnncbcdhd3443ds"
user_params = {
    "token" : TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url = pixela_endpoint, json=user_params)
# print(response.text)

# Add username to graph endpoint
graph_enpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id":"graph1",
    "name":"Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "kuro"
}

headers = {
    "X-USER-TOKEN":TOKEN
}



response = requests.post(url = graph_enpoint, json = graph_config)
print(response.text)
import requests
import datetime

pixela_endpoint = "https://pixe.la/v1/users"
username = "pratzz"
token = "cgf2cgk4cko8jhvi9"
graph_id = "graph1"

# user_params = {
#     "token": token,
#     "username": username,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }
#
# # response = requests.post(url=pixela_endpoint, json=user_params)
# # print(response.text)
#
# graph_endpoint = f"{pixela_endpoint}/{username}/graphs"
#
# graph_config = {
#     "id": graph_id,
#     "name": "Cycling Graph",
#     "unit": "km",
#     "type": "float",
#     "color": "sora"
# }
#
header = {
    "X-USER-TOKEN": token
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=header)
# print(response.text)

today = datetime.datetime.now()
habits_endpoint = f"{pixela_endpoint}/{username}/graphs/{graph_id}"

habits_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("how many kilometers did you cycle today?"),
}

response = requests.post(url=habits_endpoint, json=habits_config, headers=header)
print(response.text)

# updating pixel

update_endpoint = f"{pixela_endpoint}/{username}/graphs/{graph_id}/{today.strftime("%Y%m%d")}"

new_data = {
    "quantity": "4.5"
}

# response = requests.put(url=update_endpoint, json=new_data, headers=header)
# print(response.text)

# delete pixel
delete_endpoint = f"{pixela_endpoint}/{username}/graphs/{graph_id}/{today.strftime("%Y%m%d")}"

# response = requests.delete(url=delete_endpoint, headers=header)
# print(response.text)

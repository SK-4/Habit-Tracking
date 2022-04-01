import requests
from datetime import datetime

#datetime
x =datetime.now().strftime("%Y%m%d")

username = "sohamk"
Token = "jfkjodo43849ief"
pixela_end = "https://pixe.la/v1/users"
Graph_Id = "graph7"

user_params = {
    "token": Token,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_end,json=user_paramss)
# print(response.text)  

graph_endpoint = f"{pixela_end}/{username}/graphs"

graph_config = {
    "id": Graph_Id,
    "name": "Coding Graph",
    "unit": "Topics Covered",
    "type": "float",
    "color": "momiji"
}

headers = {
    "X-USER-TOKEN":Token
}

#response = requests.post(url=graph_endpoint,json=graph_config, headers=headers)
# print(response.text)

pixel_creation = f"{pixela_end}/{username}/graphs/{Graph_Id}"

pixel_data = {
    "name":" python",
    "date": x,
    "quantity": input("How many hours you coded today?"),
}

response = requests.post(url=pixel_creation,json=pixel_data,headers=headers)
print(response.text)

update = f"{pixela_end}/{username}/graphs/{Graph_Id}/{x}"

new_data = {}

# response = requests.delete(url=update,json=new_data,headers=headers)
# print(response.text)


delete = f"{pixela_end}/{username}/graphs/{Graph_Id}/{x}"

new_dat = {
    "name": "python",
    "quantity": "5"
}

# response = requests.delete(url=delete,json=new_dat,headers=headers)
# print(response.text)

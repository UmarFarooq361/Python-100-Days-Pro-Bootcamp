import requests
from datetime import datetime
today = datetime.now()
pixela_link = " https://pixe.la/v1/users"

token = "umar633$%@@dd"

user_token = {
    "X-USER-TOKEN" : token
}
# create user accounnt
# user_params = {
#     "token" : "umar633$%@@dd",
#     "username": "umarfarooq",
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }
# responce = requests.post(url= pixela_link, json= user_params )
# print(responce.text)

#create graph
# graph_link = "https://pixe.la/v1/users/umarfarooq/graphs"
# graph_params = {
#     "id" : "graph1",
#     "name" : "codingGraph",
#     "unit" : "hour",
#     "type" : "float",
#     "color" : "shibafu"
# }
# responce = requests.post(url= graph_link, json= graph_params , headers = user_token )
# print(responce.text)

#create pixel
pixel_params = {
    "date" : f"{today.strftime('%Y%m%d')}",
    "quantity" : input("How many hours did you code today? "),
}
add_pixel_endpoint = "https://pixe.la/v1/users/umarfarooq/graphs/graph1"
responce = requests.post(url= add_pixel_endpoint, json= pixel_params , headers = user_token )
print(responce.text)

# update pixel
# update_pixel_params = {
#     "quantity" : "4.5",
# }
# update_pixel_endpoint = f"https://pixe.la/v1/users/umarfarooq/graphs/graph1/{today.strftime('%Y%m%d')}"
# responce = requests.put(url= update_pixel_endpoint, json= update_pixel_params , headers = user_token )
# print(responce.text)

#delete pixel
# delete_pixel_endpoint = f"https://pixe.la/v1/users/umarfarooq/graphs/graph1/{today.strftime('%Y%m%d')}"
# responce = requests.delete(url= delete_pixel_endpoint , headers = user_token )
# print(responce.text)


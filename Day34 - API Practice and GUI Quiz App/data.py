import requests

parameters = {
    "amount" : 10 ,
    "type": "boolean"
}
responce = requests.get(url= "https://opentdb.com/api.php", params= parameters)
responce.raise_for_status()
question_data = responce.json()["results"]

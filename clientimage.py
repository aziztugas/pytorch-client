import requests

resp = requests.post("https://aziz-pytorch.herokuapp.com/predict", files={"file": open('C://Users/aziz/Documents/Python/Pytorch-client/dog.jpeg','rb')})

print(resp.json())
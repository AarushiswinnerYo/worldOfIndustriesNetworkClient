import os
import pickle
import requests
apiUrl="http://192.168.29.178:8000"
def main(msg, token=None, username=None, passwd=None):
    if msg=="login" and token!=None:
        r=requests.post(f"{apiUrl}/loginToken?token={token}")
    if msg=="login" and token==None:
        r=requests.post(f"{apiUrl}/login?username={username}&passwd={passwd}")
    if msg=="info":
        with open("token.pkl", "rb") as t:
            token=pickle.load(t)
        r=requests.post(f"{apiUrl}/userInfo?token={token}")
    if msg=="buyPrices":
        r=requests.post(f"{apiUrl}/buyPrices")
    if msg=="sellPrices":
        r=requests.post(f"{apiUrl}/sellPrices")
    return r.json()
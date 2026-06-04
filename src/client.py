import os
import pickle
import requests
apiUrl="https://api.woi.winnerworld.qzz.io"
def main(msg, token=None, username=None, passwd=None, amount=None, materialName=None, materialSubtype=""):
    if msg=="login" and token!=None:
        r=requests.post(f"{apiUrl}/loginToken?token={token}")
    if msg=="login" and token==None:
        r=requests.post(f"{apiUrl}/login?username={username}&passwd={passwd}")
    if msg=="info":
        with open("token.pkl", "rb") as t:
            token=pickle.load(t)
        r=requests.post(f"{apiUrl}/userInfo?token={token}")
    if msg=="buy":
        with open("token.pkl", "rb") as tk:
            token=pickle.load(tk)
        r=requests.post(f"{apiUrl}/buy?token={token}&amount={amount}&passwd={passwd}&material_name={materialName}&material_subtype={materialSubtype}")
    if msg=="buyPrices":
        r=requests.post(f"{apiUrl}/buyPrices")
    if msg=="sellPrices":
        r=requests.post(f"{apiUrl}/sellPrices")
    return r.json()
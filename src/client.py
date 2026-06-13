import os
import pickle
import requests
apiUrl="https://api.woi.winnerworld.qzz.io"
def main(msg, token=None, username=None, passwd=None, amount=None, materialName=None, materialSubtype=""):
    if msg=="login" and token!=None:
        r=requests.post(f"{apiUrl}/loginToken?token={token}")
    elif msg=="login" and token==None:
        r=requests.post(f"{apiUrl}/login?username={username}&passwd={passwd}")
    elif msg=="info":
        with open("token.pkl", "rb") as t:
            token=pickle.load(t)
        r=requests.post(f"{apiUrl}/userInfo?token={token}")
    elif msg=="buy":
        with open("token.pkl", "rb") as tk:
            token=pickle.load(tk)
        r=requests.post(f"{apiUrl}/buy?token={token}&amount={amount}&passwd={passwd}&material_name={materialName}&material_subtype={materialSubtype}")
    elif msg=="sell":
        with open("token.pkl", "rb") as tk:
            token=pickle.load(tk)
        r=requests.post(f"{apiUrl}/sell?token={token}&amount={amount}&passwd={passwd}&material_name={materialName}&material_subtype={materialSubtype}")
    elif msg=="buyPrices":
        r=requests.post(f"{apiUrl}/buyPrices")
    elif msg=="sellPrices":
        r=requests.post(f"{apiUrl}/sellPrices")
    elif msg=="craftPrices":
        r=requests.post(f"{apiUrl}/craftPrices")
    elif msg=="craft":
        with open("token.pkl", "rb") as tk:
            token=pickle.load(tk)
        r=requests.post(f"{apiUrl}/craft?token={token}&amount={amount}&passwd={passwd}&recipe_name={materialName}&recipe_subtype={materialSubtype}")
    elif msg=="sellrec":
        with open("token.pkl", "rb") as tk:
            token=pickle.load(tk)
        r=requests.post(f"{apiUrl}/sellrec?token={token}&amount={amount}&passwd={passwd}&material_name={materialName}&material_subtype={materialSubtype}")
    elif msg=="sellRecipePrices":
        r=requests.post(f"{apiUrl}/sellRecipePrices")
    return r.json()
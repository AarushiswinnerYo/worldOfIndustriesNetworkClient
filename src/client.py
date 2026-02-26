import os
import pickle
import requests
def main(msg, token=None, username=None, passwd=None):
    if msg=="login" and token!=None:
        r=requests.post(f"http://api.woi.winnerworld.qzz.io/loginToken?token={token}")
    if msg=="login" and token==None:
        r=requests.post(f"http://api.woi.winnerworld.qzz.io/login?username={username}&passwd={passwd}")
    if msg=="info":
        r=requests.post(f"http://api.woi.winnerworld.qzz.io/userInfo?username={username}")
    return r.json()
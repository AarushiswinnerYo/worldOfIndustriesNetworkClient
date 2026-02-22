import os
import pickle
import requests
def main(msg, token=None, username=None, passwd=None):
    if msg=="login" and token!=None:
        r=requests.post(f"http://192.168.29.178:8000/loginToken?token={token}")
    if msg=="login" and token==None:
        r=requests.post(f"http://192.168.29.178:8000/login?username={username}&passwd={passwd}")
    if msg=="info":
        r=requests.post(f"http://192.168.29.178:8000/userInfo?username={username}")
    return r.json()
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
        r=requests.post(f"{apiUrl}/userInfo?username={username}")
    if msg=="prices":
        r=requests.post(f"{apiUrl}/prices")
    return r.json()
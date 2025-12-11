import flet as ft
import os
import pickle

def checkLog():
    if os.path.exists("token.pkl"):
        with open("token.pkl", "rb") as f:
            tok=pickle.load(f)
    print(tok)

def retStyle():
    if os.path.exists("token.pkl"):
        return ft.TextStyle(color=ft.colors.WHITE)
    else:
        return ft.TextStyle(color=ft.colors.BLACK)
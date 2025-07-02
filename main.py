import flet as ft
import client
from threading import Thread, Event
import time
import os

DISCONNECT_MSG="!disconnect"
logged=False

def main(page: ft.Page):
    page.window.width=800
    page.window.height=600
    t=ft.Text(value="Hello, Winner")
    page.add(t)
    f=ft.Text(value="")
    page.add(f)
    def printText(f):
        t.value=str(test.value)
        page.update()
    def changeWidth(e):
        page.window.width=int(e)
        page.update()
    
    def login(user, passwd):
        log=client.main("!connect")
        r=client.main(f"login-{user}-{passwd}")
        if r=="Successfully logged in!":
            global logged
            logged=True
            t1.start()

    def closeConn(l):
        logged=False
        stop_event.set()
        t1.join()
        print("stopped")
        page.window.destroy()
        page.update()

    def getInven():
        client.main("!connect")
        log=client.main("user-Winner")
        s=client.main("show-inven")
        f.value=str(s)
        x=client.main(DISCONNECT_MSG)
        page.update()
    def updateInven(stop_Flag):
        while not stop_Flag.is_set():
            getInven()
            time.sleep(5)

    test=ft.TextField(hint_text="Username")
    Pass=ft.TextField(hint_text="Password")
    rw=ft.Row()
    page.add(test, rw)
    page.add(Pass)
    page.add(
        ft.FloatingActionButton(text="500", on_click=lambda x: changeWidth(500)),
        ft.FloatingActionButton(text="Login", on_click=lambda x:login(test.value, Pass.value)),
        ft.FloatingActionButton(text="Close", on_click=closeConn)
    )
    stop_event = Event()
    t1=Thread(target=updateInven, args=(stop_event,))


ft.app(main)
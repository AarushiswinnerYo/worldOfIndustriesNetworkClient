import flet as ft
import client

def main(page: ft.Page):
    page.window.width=800
    page.window.height=600
    page.add(ft.Text(value="Hello, Winner"))
    f=ft.Text(value="")
    page.add(f)
    def printText(f):
        f.value=str(test.value)
        page.update()
    def changeWidth(e):
        page.window.width=int(e)
        page.update()
    def getInven(l):
        client.main("!connect")
        log=client.main("user-Winner")
        s=client.main("show-inven")
        f.value=str(s)
        x=client.main("!disconnect")
        page.update()
    test=ft.TextField(hint_text="Hi?")
    rw=ft.Row(controls=[
        ft.FloatingActionButton(text="500", on_click=lambda x: changeWidth(500)),
        ft.FloatingActionButton(text="600", on_click=lambda x: changeWidth(600)),
        ft.FloatingActionButton(text="Print", on_click=printText),
        ft.FloatingActionButton(text="Test", on_click=getInven)
    ])
    page.add(test, rw)


ft.app(main)
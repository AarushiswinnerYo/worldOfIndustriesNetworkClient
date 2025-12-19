import flet as ft

def main(page: ft.Page):
    page.window.frameless=True
    page.padding=ft.padding.all(0)
    uyfwehb=ft.Container(content=ft.Text("bsiuohguwfhuiw", color=ft.Colors.BLACK),
    margin=ft.margin.symmetric(vertical=0.25),
    width=page.window.width,
    bgcolor=ft.Colors.WHITE,
    padding=ft.padding.symmetric(vertical=15, horizontal=15))
    page.add(uyfwehb, uyfwehb)
    page.bgcolor=ft.Colors.BLACK
    page.spacing=0
    uyfwehb.update()
    page.update()
ft.app(main)
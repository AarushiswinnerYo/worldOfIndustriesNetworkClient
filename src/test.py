import flet as ft

def main(page: ft.Page):
    page.add(
        ft.OutlinedButton(text="Testing", style=ft.ButtonStyle(bgcolor=ft.Colors.RED_ACCENT_700, color=ft.Colors.RED_500), disabled=True)
    )
    dia=ft.AlertDialog(
                title=ft.Text("Invalid Input"),
                content=ft.Text("Please enter a valid number."),
                actions=[ft.TextButton("Try Again", on_click=lambda x:closeDia())],
                open=True
    )
    
    def closeDia(x=None):
        dia.open=False
        page.update()
    page.add(dia)
    page.update()

ft.app(target=main)   
import flet as ft

def main(page: ft.Page):
    def handle_hover(e):
        e.control.bgcolor = ft.Colors.BLUE if e.data else ft.Colors.RED
        e.control.update()

    page.add(
        ft.Container(
            width=200,
            height=200,
            bgcolor=ft.Colors.RED,
            ink=False,
            on_hover=handle_hover,
        )
    )

ft.app(main)   
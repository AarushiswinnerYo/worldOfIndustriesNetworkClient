import flet as ft

def main(page: ft.Page):
    page.fonts={
        "Kanit": "https://raw.githubusercontent.com/google/fonts/master/ofl/kanit/Kanit-Bold.ttf"
    }
    page.theme = ft.Theme(font_family="Kanit")
    firstPage=ft.Container(
        content=ft.Column(
            controls=[
                ft.Row(alignment="spaceBetween",
                    controls=[
                        ft.Container(
                            content=ft.Icon(
                                ft.icons.MENU)),
                        ft.Row(
                            controls=[
                                ft.Icon(ft.icons.SEARCH),
                                ft.Icon(ft.icons.NOTIFICATIONS_OUTLINED)
                            ]
                        )
                    ]
                ),
                ft.Container(height=20),
                ft.Text(
                    value="HELLO!",
                    size=20
                ),
                ft.Button(
                    text="Test",
                    icon="park_rounded",
                    icon_color="green400",
                    on_click=lambda x: print("Hello :)")
                ),
                ft.IconButton(
                    icon=ft.Icons.PAUSE_CIRCLE_FILLED_ROUNDED,
                    icon_color="blue400",
                    icon_size=20,
                    tooltip="Pause record",
                    on_click=lambda x: print("Paused!")
                )
            ]
        )
    )
    page1=ft.Container()
    page2=ft.Row(
        controls=[
            ft.Container(
                width=400,
                height=850,
                bgcolor="#334a91",
                border_radius=20,
                padding=ft.padding.only(
                    top=50,left=20, right=20, bottom=5
                ),
                content=ft.Column(
                    controls=[
                        firstPage
                    ]
                )
            )
        ]
    )
    container=ft.Container(
        width=400,
        height=850,
        bgcolor="#000000",
        border_radius=15,
        content=ft.Stack(
            controls=[
                page1,
                page2
            ]
        )
        )
    page.add(ft.SafeArea(container))

ft.app(main)
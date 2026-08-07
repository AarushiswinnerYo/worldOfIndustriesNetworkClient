import flet as ft


def main(page: ft.Page):
    page.add(
        ft.SafeArea(
            content=ft.Shimmer(
                base_color=ft.Colors.with_opacity(1, "#4A009E"),
                highlight_color=ft.Colors.with_opacity(0.5, "#7317DB"),
                period=1000,
                content=ft.Column(
                    controls=[
                        ft.Container(height=20, width=100, bgcolor='#4A009E', border_radius=ft.BorderRadius.all(10)),
                        ft.Container(height=80, width=100, bgcolor='#4A009E', border_radius=ft.BorderRadius.all(10)),
                        ft.Container(height=80, width=100, bgcolor='#4A009E', border_radius=ft.BorderRadius.all(10)),
                    ],
                ),
            )
        )
    )


if __name__ == "__main__":
    ft.run(main)

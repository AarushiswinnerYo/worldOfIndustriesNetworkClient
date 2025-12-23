import flet as ft

def main(page: ft.Page):
    page.padding = 20
    page.horizontal_alignment = "left"
    page.vertical_alignment = "top"

    collapsed_w, collapsed_h = 80, 60
    expanded_w, expanded_h = 300, 260

    panel = ft.Container(
        width=collapsed_w,
        height=collapsed_h,
        bgcolor=ft.Colors.INDIGO_600,
        border_radius=14,
        padding=12,
        alignment=ft.alignment.top_left,
        animate=ft.Animation(500, "easeInOut"),
        content=ft.Text(
            "Menu",
            color=ft.Colors.WHITE,
            weight="bold"
        ),
    )

    def toggle(e):
        panel.width = expanded_w if panel.width == collapsed_w else collapsed_w
        panel.height = expanded_h if panel.height == collapsed_h else collapsed_h
        page.update()

    page.add(
        panel,
        ft.ElevatedButton("Toggle", on_click=toggle)
    )

ft.app(main)
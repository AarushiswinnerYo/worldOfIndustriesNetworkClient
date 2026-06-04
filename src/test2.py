import flet as ft


def main(page: ft.Page):
    page.title = "AlertDialog examples"

    dialog = ft.AlertDialog(
        title=ft.Text("Hello"),
        content=ft.Text("You are notified!"),
        actions=[
            ft.TextButton("Yes", on_click=lambda e: test()),
            ft.TextButton("No", on_click=lambda e: test2()),
        ],
        alignment=ft.Alignment.CENTER,
        on_dismiss=lambda e: print("Dialog dismissed!")
    )
    def test():
        loading_spinner = ft.ProgressRing(visible=True, height=10, width=10, stroke_width=1.5)
        dialog.content=ft.Row(controls=[ft.Text("loading"), loading_spinner], height=50)
        page.update()
    def test2():
        dialog.content=ft.Text("Do you really want to delete all those files?")
    modal_dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text("Please confirm"),
        content=ft.Text("Do you really want to delete all those files?"),
        actions=[
            ft.TextButton("Yes", on_click=lambda e: test()),
            ft.TextButton("No", on_click=lambda e: test2()),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        on_dismiss=lambda e: print("Modal dialog dismissed!"),
    )

    page.add(
        ft.SafeArea(
            content=ft.Column(
                controls=[
                    ft.Button(
                        content="Open dialog",
                        on_click=lambda e: page.show_dialog(dialog),
                    ),
                    ft.Button(
                        content="Open modal dialog",
                        on_click=lambda e: page.show_dialog(modal_dialog),
                    ),
                ]
            )
        )
    )


if __name__ == "__main__":
    ft.run(main)
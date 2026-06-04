import flet as ft

def main(page: ft.Page):
    page.title = "Integer Only Input Example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # 1. Positive integers only (0-9)
    positive_int_field = ft.TextField(
        label="Positive Integers Only",
        value=0,
        keyboard_type=ft.KeyboardType.NUMBER,  # Opens number pad on mobile
        input_filter=ft.InputFilter(
            allow=True, 
            regex_string=r"^[0-9]*$",            # Allows only digits
            replacement_string=""
        )
    )

    # 2. Positive & Negative integers (Allows an optional leading minus sign)
    any_int_field = ft.TextField(
        label="Positive or Negative Integers",
        value=0,
        keyboard_type=ft.KeyboardType.NUMBER,
        input_filter=ft.InputFilter(
            allow=True,
            regex_string=r"^-?[0-9]*$",       # Allows an optional '-' at the start followed by digits
            replacement_string=""
        )
    )
    def printFunc(e):
        print(positive_int_field.value)
        print(any_int_field.value)
    read_text=ft.Button(content="Print", on_click=printFunc)
    page.add(
        ft.Text("Flet Integer Input Demo", size=20, weight=ft.FontWeight.BOLD),
        positive_int_field,
        any_int_field,
        read_text
    )

ft.app(target=main)

import flet as ft

def main(page: ft.Page):
    page.title = "Smooth Slide to Sell"
    bar_width, handle_size = 300, 60
    max_x = bar_width - handle_size

    thumb = ft.Container(
        width=handle_size, height=handle_size,
        bgcolor=ft.Colors.PURPLE_ACCENT_700, border_radius=handle_size/2,
        content=ft.Icon(ft.Icons.CHEVRON_RIGHT, color="white"),
    )

    # We use a GestureDetector and update its 'left' property
    slider = ft.GestureDetector(
        content=thumb,
        left=0,
        animate_position=ft.Animation(100, ft.AnimationCurve.EASE),
        on_pan_update=lambda e: handle_move(e),
        on_pan_end=lambda e: handle_release(e),
    )

    def handle_move(e: ft.DragUpdateEvent):
        # VERSION-PROOF DELTA CHECK
        delta = 0
        try:
            if e.delta_x is not None: delta = e.delta_x
        except AttributeError:
            try:
                if e.local_delta.x is not None: delta = e.local_delta.x
            except AttributeError:
                if e.primary_delta is not None: delta = e.primary_delta

        # Apply movement
        new_left = slider.left + delta
        # Lock strictly inside [0, max_x]
        slider.left = max(0, min(new_left, max_x))
        slider.update()

    def handle_release(e: ft.DragEndEvent):
        # Snap or Confirm
        slider.animate_position = ft.Animation(600, ft.AnimationCurve.BOUNCE_OUT)
        
        if slider.left > max_x * 0.95: # 95% through the bar
            slider.left = max_x
            thumb.bgcolor = ft.Colors.GREEN_700
            thumb.content = ft.Icon(ft.Icons.CHECK, color="white")
            txt.value="Sold!"
            print("Sold!")
        else:
            slider.left = 0 # Smoothly slides back
            
        slider.update()
        thumb.update()
    txt=ft.Text("SLIDE TO SELL", weight="bold", color=ft.Colors.WHITE)

    page.add(
        ft.Stack([
            # Track
            ft.Container(
                width=bar_width, height=handle_size,
                bgcolor=ft.Colors.BLACK_45, border_radius=handle_size/2,
                alignment=ft.Alignment.CENTER,
                content=txt
            ),
            slider,
        ], 
        width=bar_width, 
        height=handle_size,
        clip_behavior=ft.ClipBehavior.HARD_EDGE # Prevents visual "escapes"
        )
    )

ft.run(targe=main, assets_dir="assets")

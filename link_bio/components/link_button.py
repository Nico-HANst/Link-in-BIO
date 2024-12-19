import reflex as rx

def link_button(text: str, url: str):
    return rx.link(
        rx.button(text),
        href=url,
        is_external=True
    )


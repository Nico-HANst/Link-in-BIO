import reflex as rx

def header():
    return rx.vstack(
        rx.avatar(name="HAN St.", fallback="HS", size="7", radius="full"),
        rx.text("@nico.hanst"),
        rx.text("BIENVENIDO A HAN STREET!! SOY NICOLÁS HUGO ADIB!"),
        rx.text('''Tengo 17 años y hace ya 8 años empecé a meterme en el mundo de la programación!'''),
        align="center"
    )

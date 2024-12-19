import reflex as rx
from link_bio.components.link_button import link_button

def links():
    return rx.vstack(
        link_button("GitHub", "https://github.com/Nico-HANst"),
        link_button("SGames_Studio", "https://scratch.mit.edu/users/SGames_Studio/"),
        link_button("Código de Ésta Página", "https://github.com/Nico-HANst/Link-in-BIO"),
        align="center"
    )


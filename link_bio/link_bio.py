import reflex as rx
from link_bio.components.navbar import navbar
from link_bio.components.footer import footer
from link_bio.views.header.header import header
from link_bio.views.links.links import links



class State(rx.State):
    pass
    


def index():
    return rx.box(
        navbar(),
        rx.vstack(
            header(),
            links(),
            align="center"
        ),
        footer()
    )


app = rx.App()
app.add_page(index)
app._compile()
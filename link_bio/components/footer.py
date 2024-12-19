import reflex as rx

def footer():
    return rx.vstack(
        rx.hstack(
            rx.image(src="favicon.ico"),
            rx.text("Mail de contacto:"),
            rx.link(
                "nicoacole@gmail.com",
                href="https://mail.google.com/mail/u/0/?ogbl#inbox?compose=CllgCHrdkkhrZMjTDFLtXmxrbhVXVkWcJvQlDBHQnntWxRJfPpxfVMxZVtFXlSVjStrTvcDgxxB",
                is_external=True
            ),
        ),
        align="center"
    )

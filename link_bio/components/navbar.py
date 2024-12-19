import reflex as rx

def navbar():
    return rx.hstack(
        rx.text(
            "HAN St.",
            height="40px"
        ),
        position="sticky",
        bg="green",
        padding_x="16px",
        padding_y="6px",
        z_index="999"
    )
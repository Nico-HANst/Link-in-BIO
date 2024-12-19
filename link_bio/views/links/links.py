import reflex as rx
from link_bio.components.link_button import link_button

def links():
    return rx.vstack(
        link_button("GitHub", "https://github.com/Nico-HANst"),
        link_button("YouTube", "https://www.youtube.com"),
        link_button("Instagram", "https://www.instagram.com"),
        link_button("Twitch", "https://www.twitch.tv"),
        align="center"
    )


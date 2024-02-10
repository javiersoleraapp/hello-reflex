"""Welcome to Reflex!."""

from hello_reflex import styles

# Import all the pages.
from hello_reflex.pages import *

import reflex as rx


class State(rx.State):
    """Define empty state to allow access to rx.State.router."""


# Create the app.
app = rx.App(style=styles.base_style)

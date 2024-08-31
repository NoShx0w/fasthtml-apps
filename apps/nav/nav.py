from fasthtml.common import *


app,rt = fast_app()

app_list = ["todo","h2f", "card3d"]

def navigation_bar(navigation_items: list[str]):
    return Nav(
        Ul(
            *[
                Li(Button(item, hx_get=f"/{item}", hx_trigger="click", hx_target="#page-content", hx_swap="innerHTML"))
                for item in navigation_items
            ]
        ),
    )


@rt("/")
def index():
    return Body(
        Div(id="page-content"),
        Footer(navigation_bar(app_list)),
        cls="footer-nav"
    )

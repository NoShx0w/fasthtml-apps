from fasthtml.common import *


hdrs = [StyleX("apps/nav/nav.css")]

app,rt = fast_app(hdrs=hdrs)

app_list = ["todo","h2f","card3d"]

def navigation_bar(navigation_items: list[str]):
    return Nav(
        Ul(
            *[
                Li(Button(item, hx_get=f"/{item}/", hx_trigger="click", hx_target="#page-content", hx_swap="outerHTML"))
                for item in navigation_items
            ]
        ),
    )


@rt("/")
def index():
    return Div(
        Div(id="page-content"),
        Div(navigation_bar(app_list)),
        cls="container"
    )

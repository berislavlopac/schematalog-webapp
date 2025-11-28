import reflex as rx
from app.pages.dashboard import dashboard_page
from app.pages.schema_list import schema_list_page
from app.pages.publish import publish_page

app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", cross_origin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap",
            rel="stylesheet",
        ),
    ],
)
app.add_page(dashboard_page, route="/")
app.add_page(schema_list_page, route="/schemas")
app.add_page(publish_page, route="/publish")
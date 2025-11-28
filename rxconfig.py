import reflex as rx

config = rx.Config(
    app_name="app",
    frontend_port=4000,
    backend_port=9000,
    plugins=[rx.plugins.sitemap.SitemapPlugin(), rx.plugins.TailwindV3Plugin()],
)

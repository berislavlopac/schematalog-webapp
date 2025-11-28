import reflex as rx


def sidebar_item(text: str, icon: str, url: str) -> rx.Component:
    """Sidebar navigation item with active state styling."""
    is_active = rx.State.router.page.path == url
    return rx.el.a(
        rx.icon(icon, class_name="h-5 w-5 mr-3"),
        rx.el.span(text, class_name="font-medium"),
        href=url,
        class_name=rx.cond(
            is_active,
            "flex items-center px-3 py-2.5 rounded-lg bg-violet-50 text-violet-700 transition-colors",
            "flex items-center px-3 py-2.5 rounded-lg text-gray-600 hover:bg-gray-50 hover:text-gray-900 transition-colors",
        ),
    )


def sidebar() -> rx.Component:
    return rx.el.aside(
        rx.el.nav(
            rx.el.div(
                rx.el.p(
                    "MENU",
                    class_name="px-3 text-xs font-semibold text-gray-400 uppercase tracking-wider mb-2",
                ),
                sidebar_item("Dashboard", "layout-dashboard", "/"),
                sidebar_item("All schemas", "layers", "/schemas"),
                sidebar_item("Publish a schema", "cloud_upload", "/publish"),
                class_name="space-y-1",
            ),
            class_name="flex flex-col gap-6",
        ),
        class_name="w-64 bg-white border-r border-gray-200 h-[calc(100vh-4rem)] p-6 hidden md:block flex-shrink-0 overflow-y-auto fixed left-0 bottom-0",
    )

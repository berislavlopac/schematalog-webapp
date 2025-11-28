import reflex as rx
from app.components.layout import layout
from app.states.schema_state import SchemaState, Schema


def stat_card(title: str, value: rx.Var | str, icon: str, color: str) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(icon, class_name=f"h-6 w-6 text-{color}-600"),
            class_name=f"p-3 bg-{color}-50 rounded-xl w-fit mb-4",
        ),
        rx.el.p(title, class_name="text-sm font-medium text-gray-500 mb-1"),
        rx.el.h3(value, class_name="text-2xl font-bold text-gray-900"),
        class_name="bg-white p-6 rounded-xl border border-gray-200 shadow-sm hover:shadow-md transition-shadow",
    )


def recent_schema_item(schema: Schema) -> rx.Component:
    return rx.el.a(
        rx.el.div(
            rx.el.h4(schema["name"], class_name="text-sm font-semibold text-gray-900"),
            rx.el.p(f"v{schema['version']}", class_name="text-xs text-gray-500 mt-0.5"),
        ),
        rx.el.span(
            schema["created_at"],
            class_name="text-xs font-medium text-gray-400 bg-gray-50 px-2 py-1 rounded-full",
        ),
        href=f"/schemas/{schema['id']}",
        class_name="flex items-center justify-between p-4 bg-white border border-gray-100 rounded-lg hover:border-violet-200 hover:shadow-sm transition-all group",
    )


def dashboard_page() -> rx.Component:
    return layout(
        rx.el.div(
            rx.el.div(
                rx.el.h1(
                    "Dashboard", class_name="text-3xl font-bold text-gray-900 mb-2"
                ),
                rx.el.p(
                    "Welcome to Schematalog. Here is an overview of your schema registry.",
                    class_name="text-gray-500",
                ),
                class_name="mb-8",
            ),
            rx.el.div(
                stat_card(
                    "Total Schemas", SchemaState.schemas.length(), "database", "violet"
                ),
                stat_card("System Status", "Operational", "activity", "green"),
                stat_card("Pending Reviews", "0", "clipboard-list", "orange"),
                class_name="grid grid-cols-1 md:grid-cols-3 gap-6 mb-10",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.el.h2(
                            "Recent Schemas",
                            class_name="text-lg font-bold text-gray-900",
                        ),
                        rx.el.a(
                            "View all",
                            href="/schemas",
                            class_name="text-sm font-medium text-violet-600 hover:text-violet-700",
                        ),
                        class_name="flex items-center justify-between mb-4",
                    ),
                    rx.el.div(
                        rx.foreach(SchemaState.recent_schemas, recent_schema_item),
                        class_name="space-y-3",
                    ),
                    class_name="col-span-2",
                ),
                rx.el.div(
                    rx.el.h2(
                        "Quick Actions",
                        class_name="text-lg font-bold text-gray-900 mb-4",
                    ),
                    rx.el.div(
                        rx.el.a(
                            rx.icon("cloud-upload", class_name="h-5 w-5 mr-3"),
                            "Publish New Schema",
                            href="/publish",
                            class_name="flex items-center w-full p-4 bg-violet-600 text-white rounded-xl font-medium hover:bg-violet-700 transition-colors shadow-sm hover:shadow mb-3",
                        ),
                        rx.el.a(
                            rx.icon(
                                "search", class_name="h-5 w-5 mr-3 text-violet-600"
                            ),
                            "Browse Catalog",
                            href="/schemas",
                            class_name="flex items-center w-full p-4 bg-white border border-gray-200 text-gray-700 rounded-xl font-medium hover:bg-gray-50 hover:border-gray-300 transition-all",
                        ),
                        class_name="flex flex-col",
                    ),
                    class_name="col-span-1",
                ),
                class_name="grid grid-cols-1 lg:grid-cols-3 gap-8",
            ),
        )
    )
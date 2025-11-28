import reflex as rx

from app.states.schema_state import Schema, SchemaState


def table_header(text: str) -> rx.Component:
    return rx.el.th(text, class_name="py-3 text-left text-sm font-bold text-gray-700")


def schema_row(schema: Schema) -> rx.Component:
    return rx.el.tr(
        rx.el.td(
            rx.el.a(
                schema["name"],
                href=f"/schemas/{schema['id']}",
                class_name="text-slate-600 hover:text-slate-800 underline decoration-slate-400 underline-offset-2",
            ),
            class_name="py-4 text-sm text-gray-900",
        ),
        rx.el.td(schema["version"], class_name="py-4 text-sm text-gray-900"),
        rx.el.td(schema["created_at"], class_name="py-4 text-sm text-gray-900"),
        class_name="border-b border-gray-100 last:border-0",
    )


def schema_table() -> rx.Component:
    return rx.el.div(
        rx.el.table(
            rx.el.thead(
                rx.el.tr(
                    table_header("Name"),
                    table_header("Current version"),
                    table_header("Created"),
                    class_name="border-b border-gray-200",
                )
            ),
            rx.el.tbody(rx.foreach(SchemaState.filtered_schemas, schema_row)),
            class_name="w-full",
        ),
        class_name="overflow-x-auto",
    )

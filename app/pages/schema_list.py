import reflex as rx
from app.components.layout import layout
from app.components.schema_table import schema_table
from app.states.schema_state import SchemaState


def schema_list_page() -> rx.Component:
    return layout(
        rx.el.div(
            rx.el.h1(
                "All schemas",
                class_name="text-3xl font-bold text-gray-800 dark:text-white mb-8",
            ),
            rx.cond(
                SchemaState.filtered_schemas.length() > 0,
                schema_table(),
                rx.el.div(
                    "No schemas found.", class_name="text-gray-500 dark:text-gray-400"
                ),
            ),
        )
    )
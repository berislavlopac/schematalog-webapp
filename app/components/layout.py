import reflex as rx
from .header import header
from .sidebar import sidebar


def layout(content: rx.Component) -> rx.Component:
    return rx.el.div(
        header(),
        rx.el.div(
            sidebar(),
            rx.el.main(
                content,
                class_name="flex-1 p-8 md:ml-64 bg-gray-50 dark:bg-slate-900 min-h-[calc(100vh-4rem)] transition-colors",
            ),
            class_name="flex flex-1",
        ),
        class_name="flex flex-col min-h-screen font-['Inter'] bg-white dark:bg-slate-900 text-gray-900 dark:text-gray-100",
    )
import reflex as rx
from .theme_toggle import theme_toggle


def header() -> rx.Component:
    return rx.el.header(
        rx.el.div(
            rx.el.a(
                rx.icon("file-json", class_name="h-8 w-8 text-violet-600 mr-2"),
                rx.el.span(
                    "Schematalog",
                    class_name="text-xl font-bold text-gray-900 dark:text-white tracking-tight",
                ),
                class_name="flex items-center",
                href="/",
            ),
            rx.el.nav(
                rx.el.div(
                    theme_toggle(),
                    class_name="mr-6 border-r border-gray-200 dark:border-slate-700 pr-6",
                ),
                rx.el.a(
                    "API Documentation",
                    rx.icon("external-link", class_name="h-4 w-4 ml-1.5"),
                    href="#",
                    target="_blank",
                    class_name="flex items-center text-sm font-medium text-gray-600 dark:text-gray-400 hover:text-violet-600 dark:hover:text-violet-400 transition-colors",
                ),
                class_name="flex items-center",
            ),
            class_name="flex items-center justify-between h-full px-6 mx-auto w-full",
        ),
        class_name="h-16 bg-white dark:bg-slate-900 border-b border-gray-200 dark:border-slate-800 sticky top-0 z-50 transition-colors",
    )
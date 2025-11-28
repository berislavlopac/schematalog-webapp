import reflex as rx
from app.states.theme_state import ThemeState


def theme_icon(icon: str, mode: str) -> rx.Component:
    return rx.el.button(
        rx.icon(icon, class_name="h-4 w-4"),
        on_click=lambda: ThemeState.set_preference(mode),
        class_name=rx.cond(
            ThemeState.preference == mode,
            "p-1.5 rounded-md bg-white dark:bg-slate-700 text-violet-600 dark:text-violet-400 shadow-sm transition-all",
            "p-1.5 rounded-md text-gray-500 dark:text-gray-400 hover:text-gray-700 dark:hover:text-gray-200 hover:bg-gray-100 dark:hover:bg-slate-800 transition-all",
        ),
        title=f"Switch to {mode} mode",
    )


def theme_toggle() -> rx.Component:
    return rx.el.div(
        theme_icon("sun", "light"),
        theme_icon("monitor", "system"),
        theme_icon("moon", "dark"),
        class_name="flex items-center gap-1 bg-gray-100 dark:bg-slate-800 p-1 rounded-lg border border-gray-200 dark:border-slate-700",
    )
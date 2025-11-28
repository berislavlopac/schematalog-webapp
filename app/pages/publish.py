import reflex as rx
from app.components.layout import layout
from app.states.publish_state import PublishState


def form_field(
    label: str,
    input_component: rx.Component,
    error: rx.Var | str = "",
    required: bool = False,
) -> rx.Component:
    return rx.el.div(
        rx.el.label(
            rx.el.span(label),
            rx.cond(required, rx.el.span(" *", class_name="text-red-500")),
            class_name="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1.5",
        ),
        input_component,
        rx.cond(
            error != "",
            rx.el.p(
                error,
                class_name="text-sm text-red-500 mt-1.5 animate-in slide-in-from-top-1 fade-in duration-200",
            ),
        ),
        class_name="mb-5",
    )


def publish_page() -> rx.Component:
    return layout(
        rx.el.div(
            rx.el.div(
                rx.el.h1(
                    "Publish a schema",
                    class_name="text-2xl font-bold text-gray-900 dark:text-white",
                ),
                rx.el.p(
                    "Create and register a new data schema to the catalog.",
                    class_name="text-gray-500 dark:text-gray-400 mt-1",
                ),
                class_name="mb-8",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.el.h2(
                            "Schema Details",
                            class_name="text-lg font-semibold text-gray-900 dark:text-white mb-4 pb-2 border-b border-gray-100 dark:border-slate-800",
                        ),
                        rx.el.div(
                            rx.el.div(
                                form_field(
                                    "Schema Name",
                                    rx.el.input(
                                        placeholder="e.g., User Profile, Order Event",
                                        on_change=PublishState.set_name,
                                        class_name=rx.cond(
                                            PublishState.name_error != "",
                                            "w-full px-4 py-2.5 bg-white dark:bg-slate-900 border border-red-300 dark:border-red-800/60 rounded-lg focus:outline-none focus:ring-2 focus:ring-red-500/20 focus:border-red-500 transition-all text-gray-900 dark:text-white",
                                            "w-full px-4 py-2.5 bg-white dark:bg-slate-900 border border-gray-200 dark:border-slate-700 rounded-lg focus:outline-none focus:ring-2 focus:ring-violet-500/20 focus:border-violet-500 transition-all text-gray-900 dark:text-white",
                                        ),
                                        default_value=PublishState.name,
                                    ),
                                    error=PublishState.name_error,
                                    required=True,
                                ),
                                class_name="col-span-2",
                            ),
                            rx.el.div(
                                form_field(
                                    "Version",
                                    rx.el.input(
                                        placeholder="e.g., 1.0.0",
                                        on_change=PublishState.set_version,
                                        class_name=rx.cond(
                                            PublishState.version_error != "",
                                            "w-full px-4 py-2.5 bg-white dark:bg-slate-900 border border-red-300 dark:border-red-800/60 rounded-lg focus:outline-none focus:ring-2 focus:ring-red-500/20 focus:border-red-500 transition-all text-gray-900 dark:text-white",
                                            "w-full px-4 py-2.5 bg-white dark:bg-slate-900 border border-gray-200 dark:border-slate-700 rounded-lg focus:outline-none focus:ring-2 focus:ring-violet-500/20 focus:border-violet-500 transition-all text-gray-900 dark:text-white",
                                        ),
                                        default_value=PublishState.version,
                                    ),
                                    error=PublishState.version_error,
                                    required=True,
                                ),
                                class_name="col-span-1",
                            ),
                            class_name="grid grid-cols-1 md:grid-cols-3 gap-x-6",
                        ),
                        form_field(
                            "Author",
                            rx.el.input(
                                placeholder="e.g., Engineering Team",
                                on_change=PublishState.set_author,
                                class_name="w-full px-4 py-2.5 bg-white dark:bg-slate-900 border border-gray-200 dark:border-slate-700 rounded-lg focus:outline-none focus:ring-2 focus:ring-violet-500/20 focus:border-violet-500 transition-all text-gray-900 dark:text-white",
                                default_value=PublishState.author,
                            ),
                        ),
                        form_field(
                            "Description",
                            rx.el.textarea(
                                placeholder="Describe what this schema represents...",
                                on_change=PublishState.set_description,
                                rows=3,
                                class_name="w-full px-4 py-2.5 bg-white dark:bg-slate-900 border border-gray-200 dark:border-slate-700 rounded-lg focus:outline-none focus:ring-2 focus:ring-violet-500/20 focus:border-violet-500 transition-all resize-y text-gray-900 dark:text-white",
                                default_value=PublishState.description,
                            ),
                        ),
                        form_field(
                            "Tags",
                            rx.el.input(
                                placeholder="e.g., analytics, core, legacy (comma separated)",
                                on_change=PublishState.set_tags,
                                class_name="w-full px-4 py-2.5 bg-white dark:bg-slate-900 border border-gray-200 dark:border-slate-700 rounded-lg focus:outline-none focus:ring-2 focus:ring-violet-500/20 focus:border-violet-500 transition-all text-gray-900 dark:text-white",
                                default_value=PublishState.tags,
                            ),
                        ),
                        rx.el.div(
                            rx.el.h2(
                                "Schema Definition",
                                class_name="text-lg font-semibold text-gray-900 dark:text-white mb-4 mt-8 pb-2 border-b border-gray-100 dark:border-slate-800",
                            ),
                            form_field(
                                "Content (JSON/YAML)",
                                rx.el.div(
                                    rx.el.textarea(
                                        placeholder="""{
  "type": "record",
  "name": "User",
  "fields": [...]
}""",
                                        on_change=PublishState.set_content,
                                        class_name="w-full h-80 px-4 py-4 bg-slate-900 dark:bg-black text-slate-50 font-mono text-sm rounded-lg focus:outline-none focus:ring-2 focus:ring-violet-500/50 focus:border-violet-500 transition-all leading-relaxed",
                                        spellcheck=False,
                                        default_value=PublishState.content,
                                    ),
                                    rx.el.p(
                                        "Paste your schema definition here. JSON format is recommended.",
                                        class_name="text-xs text-gray-500 dark:text-gray-400 mt-2",
                                    ),
                                ),
                                error=PublishState.content_error,
                                required=True,
                            ),
                        ),
                        rx.el.div(
                            rx.el.button(
                                "Cancel",
                                on_click=PublishState.cancel,
                                type="button",
                                class_name="px-6 py-2.5 border border-gray-300 dark:border-slate-600 text-gray-700 dark:text-gray-300 font-medium rounded-lg hover:bg-gray-50 dark:hover:bg-slate-800 focus:ring-4 focus:ring-gray-100 dark:focus:ring-slate-800 transition-all",
                            ),
                            rx.el.button(
                                rx.cond(
                                    PublishState.is_loading,
                                    rx.el.span(
                                        rx.icon(
                                            "loader",
                                            class_name="animate-spin h-4 w-4 mr-2 inline",
                                        ),
                                        "Publishing...",
                                    ),
                                    rx.el.span(
                                        rx.icon(
                                            "cloud-upload",
                                            class_name="h-4 w-4 mr-2 inline",
                                        ),
                                        "Publish Schema",
                                    ),
                                ),
                                on_click=PublishState.handle_submit,
                                disabled=PublishState.is_loading,
                                class_name="px-6 py-2.5 bg-violet-600 text-white font-medium rounded-lg hover:bg-violet-700 focus:ring-4 focus:ring-violet-500/30 transition-all shadow-sm disabled:opacity-70 disabled:cursor-not-allowed flex items-center",
                            ),
                            class_name="flex items-center justify-end gap-4 mt-8 pt-6 border-t border-gray-100 dark:border-slate-800",
                        ),
                    ),
                    class_name="bg-white dark:bg-slate-800 p-6 md:p-8 rounded-xl border border-gray-200 dark:border-slate-700 shadow-sm transition-all",
                ),
                class_name="max-w-4xl mx-auto",
            ),
        )
    )
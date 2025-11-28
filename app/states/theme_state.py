import reflex as rx


class ThemeState(rx.State):
    preference: str = rx.Cookie("system", name="theme_preference")
    theme_mode: str = "light"

    @rx.event
    async def initialize_theme(self):
        """Initialize the theme based on preference on page load."""
        if not self.preference:
            self.preference = "system"
        if self.preference == "system":
            yield rx.call_script(
                "window.matchMedia('(prefers-color-scheme: dark)').matches",
                callback=ThemeState.update_system_mode,
            )
        elif self.preference == "dark":
            self.theme_mode = "dark"
        else:
            self.theme_mode = "light"

    @rx.event
    def update_system_mode(self, is_dark: bool):
        """Callback from JS to set mode based on system preference."""
        self.theme_mode = "dark" if is_dark else "light"

    @rx.event
    async def set_preference(self, pref: str):
        """Set the theme preference and update the theme_mode."""
        self.preference = pref
        if pref == "system":
            yield rx.call_script(
                "window.matchMedia('(prefers-color-scheme: dark)').matches",
                callback=ThemeState.update_system_mode,
            )
        elif pref == "dark":
            self.theme_mode = "dark"
        else:
            self.theme_mode = "light"
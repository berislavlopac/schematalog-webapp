import reflex as rx
import json
import random
import string
import logging
from datetime import datetime
from app.states.schema_state import SchemaState


class PublishState(rx.State):
    name: str = ""
    version: str = ""
    description: str = ""
    tags: str = ""
    author: str = ""
    content: str = ""
    name_error: str = ""
    version_error: str = ""
    content_error: str = ""
    is_loading: bool = False

    @rx.event
    def set_name(self, value: str):
        self.name = value
        if self.name_error:
            self.name_error = ""

    @rx.event
    def set_version(self, value: str):
        self.version = value
        if self.version_error:
            self.version_error = ""

    @rx.event
    def set_content(self, value: str):
        self.content = value
        if self.content_error:
            self.content_error = ""

    @rx.event
    async def handle_submit(self):
        self.is_loading = True
        self.name_error = ""
        self.version_error = ""
        self.content_error = ""
        has_error = False
        if not self.name.strip():
            self.name_error = "Schema name is required"
            has_error = True
        if not self.version.strip():
            self.version_error = "Version is required"
            has_error = True
        if not self.content.strip():
            self.content_error = "Schema content is required"
            has_error = True
        else:
            try:
                json.loads(self.content)
            except ValueError as e:
                logging.exception(f"Error validating JSON: {e}")
                trimmed = self.content.strip()
                if trimmed.startswith("{") or trimmed.startswith("["):
                    self.content_error = "Invalid JSON format"
                    has_error = True
        if has_error:
            self.is_loading = False
            yield rx.toast.error("Please fix the errors in the form.")
            return
        rand_suffix = "".join(
            random.choices(string.digits + string.ascii_lowercase, k=6)
        )
        schema_id = f"sch_{rand_suffix}"
        tags_list = [t.strip() for t in self.tags.split(",") if t.strip()]
        new_schema = {
            "id": schema_id,
            "name": self.name,
            "version": self.version,
            "description": self.description,
            "tags": tags_list,
            "created_at": datetime.now().strftime("%d %B %Y %H:%M"),
            "author": self.author or "Anonymous",
            "content": self.content,
        }
        schema_state = await self.get_state(SchemaState)
        schema_state.add_schema(new_schema)
        self.is_loading = False
        self.name = ""
        self.version = ""
        self.description = ""
        self.tags = ""
        self.author = ""
        self.content = ""
        yield rx.toast.success("Schema published successfully!")
        yield rx.redirect("/")

    @rx.event
    def cancel(self):
        self.name = ""
        self.version = ""
        self.description = ""
        self.tags = ""
        self.author = ""
        self.content = ""
        self.name_error = ""
        self.version_error = ""
        self.content_error = ""
        return rx.redirect("/")
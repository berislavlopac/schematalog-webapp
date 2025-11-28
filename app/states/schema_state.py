from typing import TypedDict

import reflex as rx


class Schema(TypedDict):
    id: str
    name: str
    version: str
    description: str
    tags: list[str]
    created_at: str
    author: str
    content: str


class SchemaState(rx.State):
    schemas: list[Schema] = [
        {
            "id": "sch_001",
            "name": "ieu.association",
            "version": "1.0",
            "description": "",
            "tags": [],
            "created_at": "05 June 2023 20:23",
            "author": "",
            "content": "{}",
        },
        {
            "id": "sch_002",
            "name": "ieu.device",
            "version": "1.0",
            "description": "",
            "tags": [],
            "created_at": "05 June 2023 21:55",
            "author": "",
            "content": "{}",
        },
        {
            "id": "sch_003",
            "name": "ieu.raw.entity",
            "version": "1.0",
            "description": "",
            "tags": [],
            "created_at": "05 June 2023 21:57",
            "author": "",
            "content": "{}",
        },
        {
            "id": "sch_004",
            "name": "ieu.vehicle",
            "version": "1.0",
            "description": "",
            "tags": [],
            "created_at": "05 June 2023 21:56",
            "author": "",
            "content": "{}",
        },
        {
            "id": "sch_005",
            "name": "test",
            "version": "1.2",
            "description": "",
            "tags": [],
            "created_at": "20 June 2023 08:25",
            "author": "",
            "content": "{}",
        },
    ]
    search_query: str = ""

    @rx.var
    def filtered_schemas(self) -> list[Schema]:
        """Filter schemas based on search query."""
        filtered = self.schemas
        if self.search_query:
            query = self.search_query.lower()
            filtered = [
                s
                for s in filtered
                if query in s["name"].lower() or query in s["description"].lower()
            ]
        return filtered

    @rx.var
    def recent_schemas(self) -> list[Schema]:
        """Get the 3 most recent schemas."""
        return self.schemas[:3]

    @rx.event
    def set_search_query(self, query: str):
        self.search_query = query

    @rx.event
    def add_schema(self, schema: Schema):
        """Add a new schema to the list."""
        self.schemas.insert(0, schema)

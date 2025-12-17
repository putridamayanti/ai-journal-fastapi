from typing import Any

def build_list_pagination_response(
        items: list[Any],
        total_items: int,
        offset: int,
        limit: int
) -> dict[str, Any]:
    return {
        "total": total_items,
        "offset": offset,
        "limit": limit,
        "items": items
    }
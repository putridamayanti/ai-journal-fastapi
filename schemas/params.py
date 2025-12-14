from fastapi import Query
from sqlmodel import SQLModel

class PaginationParams(SQLModel):
    skip: int = 0
    limit: int = 100

class DefaultListParams(PaginationParams):
    search: str | None = Query(default=None, description="Search term to filter results")
    order_by: str | None = Query(default="desc", pattern="^(asc|desc)$", description="Sort by field")
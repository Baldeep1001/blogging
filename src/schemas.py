from pydantic import BaseModel
from datetime import datetime
from typing import List

class BlogPostBase(BaseModel):
    title: str
    content: str
    category: str
    tags: List[str]

class BlogPostCreate(BlogPostBase):
    pass

class BlogPostResponse(BlogPostBase):
    id: int
    createdAt: datetime
    updatedAt: datetime

    class Config:
        from_attributes = True

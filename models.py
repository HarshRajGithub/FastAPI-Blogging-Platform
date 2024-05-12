from pydantic import BaseModel
from typing import List, Optional

class BlogPost(BaseModel):
    title: str
    content: str
    author: str
    comments: List[str] = []

class Comment(BaseModel):
    text: str
    author: str

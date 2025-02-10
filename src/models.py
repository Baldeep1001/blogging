from .database import Base
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

class BlogPost(Base):
    _tablename_ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String)
    category = Column(String, index=True)
    tags = Column(String)
    createdAt = Column(DateTime, default=datetime.utcnow)
    updatedAt = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

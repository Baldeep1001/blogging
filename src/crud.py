from sqlalchemy.orm import Session
from . import models, schemas

def create_post(db: Session, post: schemas.BlogPostCreate):
    new_post = models.BlogPost(
        title=post.title,
        content=post.content,
        category=post.category,
        tags=",".join(post.tags)
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

def get_posts(db: Session, term: str = None):
    query = db.query(models.BlogPost)
    if term:
        query = query.filter(models.BlogPost.title.contains(term) |
                             models.BlogPost.content.contains(term) |
                             models.BlogPost.category.contains(term))
    return query.all()

def get_post(db: Session, post_id: int):
    return db.query(models.BlogPost).filter(models.BlogPost.id == post_id).first()

def delete_post(db: Session, post_id: int):
    post = db.query(models.BlogPost).filter(models.BlogPost.id == post_id).first()
    if post:
        db.delete(post)
        db.commit()
    return post

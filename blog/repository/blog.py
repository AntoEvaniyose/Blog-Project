from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, models


def get_all(db: Session):
    blogs=db.query(models.Blog).all()
    return blogs

def create(request: schemas.Blog, db: Session, current_user):
    new_blog=models.Blog(title=request.title, description=request.description,user_id=current_user.id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def destroy(id:int, db: Session, user_id: int):
    blog=db.query(models.Blog).filter(models.Blog.id == id, models.Blog.user_id == user_id)
    if not blog.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail=f"Blog with id {id} not found or you do not have permission to delete it.")
    blog.delete(synchronize_session=False)
    db.commit()
    return 'Deleted Successfully'

def update(id:int,request:schemas.Blog, db:Session, user_id: int):
    blog = db.query(models.Blog).filter(models.Blog.id == id, models.Blog.user_id == user_id)
    if not blog.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail=f"Blog with id {id} not found or you do not have permission to edit it.")
    blog.update(request.dict())
    db.commit()
    return 'Updated successfully'

def show(id:int, db:Session, user_id: int):
    blog=db.query(models.Blog).filter(models.Blog.id == id, models.Blog.user_id == user_id).first()
    if not blog:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail=f"Blog with the id {id} is not available or you do not have permission to view it.")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail':f"Blog with the id {id} is not available"}
    return blog
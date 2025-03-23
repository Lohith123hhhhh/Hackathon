
from typing import List
from fastapi import Depends,HTTPException,APIRouter
from starlette import status
from app import models, oauth2, schemas
from app.database import  get_db
from sqlalchemy.orm import Session



router = APIRouter(
    prefix="/feedbacks",
)


@router.get("/", response_model=List[schemas.FeedbackCreate], status_code=status.HTTP_200_OK)
def get_posts(db: Session = Depends(get_db)):
    feedback = db.query(models.Feedback).all()
    return feedback

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.FeedbackCreate)
def create_posts(feedback: schemas.Feedback, db: Session = Depends(get_db), user_current: int = Depends(
    oauth2.get_current_user)):
    new_post = models.Feedback(user_id=user_current.id, **feedback.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.FeedbackCreate)
def get_post(id: int,db: Session = Depends(get_db)):
    feedbacks = db.query(models.Feedback).filter(models.Feedback.id == id).first()
    if not feedbacks:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    return feedbacks

@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db), user_current: int = Depends(oauth2.get_current_user)):
    feedback_query = db.query(models.Feedback).filter(models.Feedback.id == id)
    feedbacks = feedback_query.first()
    if not feedbacks:
        raise HTTPException(status_code=404, detail="Post not found")
    if feedbacks.user_id != user_current.id:
        raise HTTPException(status_code=403, detail="You are not the owner of the post")
    feedback_query.delete(synchronize_session=False)
    db.commit()
    return {"message": "Post deleted"}

@router.put("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.FeedbackCreate)
def update_post(feedback: schemas.Feedback, id: int, db: Session = Depends(get_db), user_current: int = Depends(
    oauth2.get_current_user)):
    feedback_query = db.query(models.Feedback).filter(models.Feedback.id == id)
    feedbacks = feedback_query.first()
    if feedbacks is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Post not found")
    if feedbacks.user_id != user_current.id:
        raise HTTPException(status_code=403, detail="You are not the owner of the post")
    feedback_query.update(feedback.dict(), synchronize_session=False)
    db.commit()
    return feedback_query.first()
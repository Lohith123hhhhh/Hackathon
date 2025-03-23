
from typing import List
from fastapi import Depends,HTTPException,APIRouter
from starlette import status
from app import models, oauth2, schemas
from app.database import  get_db
from sqlalchemy.orm import Session



router = APIRouter(
    prefix="/events",
)


@router.get("/", response_model=List[schemas.Event], status_code=status.HTTP_200_OK)
def get_posts(db: Session = Depends(get_db)):
    events = db.query(models.Events).all()
    return events

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Event)
def create_posts(events: schemas.EventsCreate, db: Session = Depends(get_db), admin_current: int = Depends(
    oauth2.get_current_admin)):
    new_post = models.Events(admin_id=admin_current.id, **events.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.Event)
def get_post(id: int,db: Session = Depends(get_db)):
    events = db.query(models.Events).filter(models.Events.id == id).first()
    if not events:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    return events

@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db), admin_current: int = Depends(oauth2.get_current_admin)):
    events_query = db.query(models.Events).filter(models.Events.id == id)
    events = events_query.first()
    if not events:
        raise HTTPException(status_code=404, detail="Post not found")
    if events.admin_id != admin_current.id:
        raise HTTPException(status_code=403, detail="You are not the owner of the post")
    events_query.delete(synchronize_session=False)
    db.commit()
    return {"message": "Post deleted"}

@router.put("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.Event)
def update_post(event: schemas.EventsCreate, id: int, db: Session = Depends(get_db), admin_current: int = Depends(
    oauth2.get_current_admin)):
    event_query = db.query(models.Events).filter(models.Events.id == id)
    events = event_query.first()
    if events is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Post not found")
    if events.admin_id != admin_current.id:
        raise HTTPException(status_code=403, detail="You are not the owner of the post")
    event_query.update(event.dict(), synchronize_session=False)
    db.commit()
    return event_query.first()

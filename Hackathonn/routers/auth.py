from fastapi import APIRouter, Depends, HTTPException
from app import hashing, models, oauth2, schemas
from app.database import get_db
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/login",
)

@router.post("/")
def login(user_credentials: schemas.AuthenticateUser, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == user_credentials.email).first()
    if not user:
        raise HTTPException(status_code=403, detail="User not found")

    if not hashing.verify_password(user_credentials.password, user.password):
        raise HTTPException(status_code=403, detail="Incorrect password")

    token = oauth2.create_token(data={"user_id": user.id})
    return {"token": token, "token_type":"bearer"}

@router.post("/admin")
def login(admin_credentials: schemas.AuthenticateAdmin, db: Session = Depends(get_db)):
    admin = db.query(models.Admin).filter(models.Admin.email == admin_credentials.email).first()
    if not admin:
        raise HTTPException(status_code=403, detail="User not found")

    if not hashing.verify_password(admin_credentials.password, admin.password):
        raise HTTPException(status_code=403, detail="Incorrect password")

    token = oauth2.create_token(data={"admin_id": admin.id})
    return {"token": token, "token_type":"bearer"}
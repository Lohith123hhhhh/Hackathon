from datetime import datetime

from pydantic import BaseModel, EmailStr




class CreateUser(BaseModel):
    email: EmailStr
    password: str
    class Config:
        orm_mode = True

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    class Config:
        orm_mode = True


class AuthenticateUser(BaseModel):
    email: EmailStr
    password: str
    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

    class Config:
        orm_mode = True

class TokenData(BaseModel):
    id: int

class AuthenticateAdmin(BaseModel):
    email: EmailStr
    password: str
    class Config:
        orm_mode = True

class Event(BaseModel):
    description: str
    name_event: str
    organizer_name: str
    class Config:
        orm_mode = True

class EventsCreate(Event):
    pass

class Feedback(BaseModel):
    comment: str
    rating: str
    event_id: int
    class Config:
        orm_mode = True

class FeedbackCreate(Feedback):
    created_at: datetime
    class Config:
        orm_mode = True
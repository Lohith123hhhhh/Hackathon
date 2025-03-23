from fastapi import FastAPI,APIRouter
from app import models
from app.database import engine
from routers import users,auth,events,feedback
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)
app.include_router(auth.router)
app.include_router(events.router)
app.include_router(feedback.router)

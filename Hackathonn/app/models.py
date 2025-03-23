from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP,ForeignKey
from sqlalchemy.sql.expression import text
from app.database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True,nullable=False)
    email = Column(String, nullable=False,unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False,server_default=text('now()'))

class Admin(Base):
    __tablename__ = 'admins'
    id = Column(Integer, primary_key=True,nullable=False)
    email = Column(String, nullable=False,unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False,server_default=text('now()'))

class Events(Base):
    __tablename__ = 'events'
    id = Column(Integer, primary_key=True,nullable=False)
    name_event = Column(String, nullable=False)
    description = Column(String, nullable=False)
    organizer_name = Column(String, nullable=False)
    admin_id = Column(Integer, ForeignKey('admins.id', ondelete='CASCADE'),nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False,server_default=text('now()'))

class Feedback(Base):
    __tablename__ = 'feedback'
    id = Column(Integer, primary_key=True,nullable=False)
    comment = Column(String, nullable=False)
    rating = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'),nullable=False)
    event_id = Column(Integer, ForeignKey('events.id', ondelete='CASCADE'),nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False,server_default=text('now()'))
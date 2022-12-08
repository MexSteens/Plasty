from app.database import db
from sqlalchemy_tables_extended import BaseModel
from sqlalchemy import Column, String, TIMESTAMP, func, ForeignKey, Integer
from app.database.model import User, Achievement


class Table(db.Model, BaseModel):
    __tablename__ = 'user_achievement'
    __session__ = db.session

    user_id = Column(String(36), ForeignKey(User.id), primary_key=True)
    achievement_code = Column(String(16), ForeignKey(Achievement.code), primary_key=True)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    last_modified = Column(TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp(), nullable=False)

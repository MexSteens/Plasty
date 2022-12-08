from app.database import db
from sqlalchemy_tables_extended import BaseModel
from sqlalchemy import Column, String, TIMESTAMP, func, Text, Integer


class Table(db.Model, BaseModel):
    __tablename__ = 'achievement'
    __session__ = db.session

    code = Column(String(16), primary_key=True)
    name = Column(String(128), nullable=False, unique=True)
    description = Column(Text)
    experience_given = Column(Integer)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    last_modified = Column(TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp(), nullable=False)

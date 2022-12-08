from app.database import db
from sqlalchemy_tables_extended import BaseModel
from sqlalchemy import Column, String, Integer, ForeignKey, TIMESTAMP, func, and_
from app.database.model import User, Product


class Table(db.Model, BaseModel):
    __tablename__ = 'complaint'
    __session__ = db.session
    __order_columns__ = {
        'code': 'ASC'
    }

    id = Column(Integer, primary_key=True)
    user_id = Column(String(36), ForeignKey(User.id))
    product_id = Column(Integer, ForeignKey(Product.id), nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    last_modified = Column(TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp(), nullable=False)

    @classmethod
    def read_date(cls, user_id, date):
        return cls.query.filter(and_(func.date(cls.created_at) == date, cls.user_id == user_id)).all()

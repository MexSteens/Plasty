from app.database import db
from sqlalchemy_tables_extended import BaseModel
from sqlalchemy import Column, String, Integer, TIMESTAMP, func


class Table(db.Model, BaseModel):
    __tablename__ = 'company'
    __session__ = db.session
    __order_columns__ = {
        'code': 'ASC'
    }

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False, unique=True)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    last_modified = Column(TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp(), nullable=False)

    def read_products(self):
        from app.database.model import Product

        query = self.__session__.query(Product).filter(Product.company_id == self.id).all()

        return query

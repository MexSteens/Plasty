from app.database import db
from sqlalchemy_tables_extended import BaseModel
from sqlalchemy import Column, String, Integer, ForeignKey, TIMESTAMP, func
from app.database.model import Company


class Table(db.Model, BaseModel):
    __tablename__ = 'product'
    __session__ = db.session
    __order_columns__ = {
        'code': 'ASC'
    }

    id = Column(Integer, primary_key=True)
    company_id = Column(Integer, ForeignKey(Company.id), nullable=False, unique=True)
    name = Column(String(128), nullable=False, unique=True)
    barcode = Column(String(32), nullable=False, unique=True)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    last_modified = Column(TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp(), nullable=False)

    def read_complaints(self, limit=50):
        from app.database.model import Complaint

        query = self.__session__.query(Complaint).filter(Complaint.product_id == self.id).limit(limit).all()

        return query

    def total_complaints(self):
        from app.database.model import Complaint

        query = self.__session__.query(Complaint).filter(Complaint.product_id == self.id).count()

        return query

    def new_complaint(self, user_id=None):
        from app.database.model import Complaint

        complaint = Complaint(product_id=self.id, user_id=user_id)

        complaint.create()

        return complaint

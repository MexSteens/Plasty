from app.database import db
from sqlalchemy_tables_extended import BaseModel
from sqlalchemy import Column, String, TIMESTAMP, func, Boolean, Integer
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import uuid


class Table(db.Model, BaseModel):
    __tablename__ = 'user'
    __session__ = db.session

    id = Column(String(36), primary_key=True)
    name = Column(String(128), nullable=False, unique=True)
    email = Column(String(320), nullable=False, unique=True)
    password = Column(String(4096), nullable=False)
    admin = Column(Boolean, nullable=False, default=False)
    last_login = Column(TIMESTAMP)
    level = Column(Integer, nullable=False, default=1)
    experience = Column(Integer, nullable=False, default=0)
    streaks = Column(Integer, nullable=False, default=0)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    last_modified = Column(TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp(), nullable=False)

    def set_password(self, password):
        self.password = generate_password_hash(password, 'sha256')

    def validate_password(self, password):
        return check_password_hash(self.password, password)

    def update_last_login(self):
        self.last_login = datetime.now()

        self.update()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    @classmethod
    def authenticate(cls, email, password):
        user = cls.get(email=email)

        if not user:
            raise LookupError

        if not user.validate_password(password):
            raise UserWarning

        user.update_last_login()

        return user

    def level_up(self, amount=1):
        self.level += amount

    def exp_needed(self):
        return self.level * 110

    def exp_gain(self, experience):
        self.experience += experience

    def identity(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "admin": self.admin,
            "last_login": self.last_login,
            "level": self.level,
            "experience": self.experience,
            "experience_needed": self.exp_needed(),
            "streaks": self.streaks,
            "achievements": self.get_achievements(),
            "created_at": self.created_at,
            "last_modified": self.last_modified
        }

    def generate_uuid(self):
        new_uuid = uuid.uuid4()

        self.id = new_uuid

    def create(self, _no_commit=False, **kwargs):
        self.generate_uuid()

        # Run Base model create method
        super().create(_no_commit=_no_commit, **kwargs)

    def scanned_products(self):
        from app.database.model import Product, Complaint

        query = self.__session__.query(Product).join(Complaint, Complaint.product_id == Product.id).filter(Complaint.user_id == self.id).all()

        return query

    def get_achievements(self):
        from app.database.model import UserAchievement

        query = self.__session__.query(UserAchievement).filter(self.id == UserAchievement.user_id).all()

        return [row.achievement_code for row in query]

    # def get_non_owned_achievements(self):
    #     from app.database.model import UserAchievement
    #
    #     query = self.__session__.query(UserAchievement).filter(self.id == UserAchievement.user_id).all()
    #
    #     return [row.achievement_code for row in query]

    def reward_achievement(self, achievement_code):
        from app.database.model import Achievement, UserAchievement

        new_achievement = UserAchievement(user_id=self.id, achievement_code=achievement_code)
        new_achievement.create()

        achievement = Achievement.get(code=achievement_code)
        self.exp_gain(achievement.experience_given)


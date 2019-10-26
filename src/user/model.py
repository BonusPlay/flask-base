from enum import IntEnum
from src import db, bcrypt, ma
from marshmallow_enum import EnumField  # type: ignore


class Roles(IntEnum):
    pleb = 0
    admin = 1


class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(255), unique=True, nullable=False, index=True)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.Enum(Roles))

    def __init__(self, username, password, role=Roles.pleb) -> None:
        self.username = username
        self.role = role
        self.set_password(password)

    def set_password(self, password) -> None:
        self.password = bcrypt.generate_password_hash(password=password).decode()

    def check_password(self, password) -> bool:
        return bcrypt.check_password_hash(self.password, password)

    def is_authorized(self, claims) -> bool:
        return self.is_admin() or claims['identity'] in self.id

    def is_admin(self) -> bool:
        return Roles.admin in self.role

    @classmethod
    def find_by_id(cls, user_id):
        return cls.query.filter_by(id=user_id).first()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()


class UserSchema(ma.ModelSchema):
    """
    Do not use this class on your own, instead, use instantiated methods below
    """
    role = EnumField(Roles)

    class Meta:
        model = User


user_schema = UserSchema(exclude=('password',))
users_schema = UserSchema(exclude=('password',), many=True)

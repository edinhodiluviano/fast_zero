import sqlalchemy.orm
from sqlalchemy.orm import Mapped


class Base(sqlalchemy.orm.DeclarativeBase):
    ...


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = sqlalchemy.orm.mapped_column(primary_key=True)
    username: Mapped[str]
    password: Mapped[str]
    email: Mapped[str]

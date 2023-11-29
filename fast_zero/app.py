import fastapi
from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from fast_zero import models, schemas
from fast_zero.database import get_session


app = fastapi.FastAPI()
database = []


@app.get('/')
def read_root():
    return {'message': 'olá mundo'}


@app.post('/users/', status_code=201, response_model=schemas.UserPublic)
def create_user(
    user: schemas.UserSchema,
    session: Session = Depends(get_session),
):
    db_user = session.scalar(
        select(models.User).where(models.User.username == user.username)
    )

    if db_user:
        raise fastapi.HTTPException(
            status_code=400, detail='Username already registered'
        )

    db_user = models.User(
        username=user.username,
        password=user.password,
        email=user.email,
    )
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user


@app.get('/users/', response_model=schemas.UserList)
def read_users(session: Session = Depends(get_session)):
    users = session.scalars(select(models.User)).all()
    return {'users': users}


@app.put('/users/{user_id}', response_model=schemas.UserPublic)
def update_user(user_id: int, user: schemas.UserSchema):
    if user_id > len(database) or user_id < 1:
        raise fastapi.HTTPException(404, detail='User not found')
    user_with_id = schemas.UserDB(**user.model_dump(), id=user_id)
    database[user_id - 1] = user_with_id

    return user_with_id


@app.delete('/users/{user_id}', response_model=schemas.Message)
def delete_user(user_id: int):
    if user_id > len(database) or user_id < 1:
        raise fastapi.HTTPException(404, detail='User not found')

    del database[user_id - 1]
    return dict(detail='user deleted')

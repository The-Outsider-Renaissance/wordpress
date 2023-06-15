from fastapi import HTTPException
from sqlalchemy.orm import Session

import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_users(db: Session, limit: int = 100, is_active: bool | None = None):
    query = db.query(models.User)

    if is_active is not None:
        query = query.filter(models.User.is_active == is_active)

    return query.limit(limit).all()


def create_user(db: Session, user: schemas.User):
    db_user = models.User(
        name=user.name, title=user.title, avatar=user.avatar, is_active=user.is_active
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def edit_user(db: Session, user_id: int, user: schemas.UpdateUser):
    db_user = get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    for var, value in vars(user).items():
        setattr(db_user, var, value) if value is not None else None

    db.commit()
    db.refresh(db_user)
    return db_user

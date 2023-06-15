from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal, engine
import crud, models, schemas

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def healthcheck():
    return {"status": "ok"}


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.User, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)


@app.patch("/users/{user_id}", response_model=schemas.User)
def edit_user(user_id: int, user: schemas.UpdateUser, db: Session = Depends(get_db)):
    return crud.edit_user(db=db, user_id=user_id, user=user)


@app.get("/users/", response_model=list[schemas.User])
def read_users(
    limit: int = 100, is_active: bool | None = None, db: Session = Depends(get_db)
):
    users = crud.get_users(db, limit=limit, is_active=is_active)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

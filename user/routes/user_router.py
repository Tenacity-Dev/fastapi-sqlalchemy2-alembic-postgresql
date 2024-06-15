from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from core.database import get_db
from user.schemas.user import UserSchema, UserCreate
from user.services.user_service import get_users, create_user, get_user, delete_user

user_router = APIRouter()


@user_router.get('/users', response_model=list[UserSchema])
def user_list(db: Session = Depends(get_db)):
    db_users = get_users(db)

    return db_users


@user_router.get('/users/{user_id}', response_model=UserSchema)
def user_detail(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return db_user


@user_router.delete('/users/{user_id}')
def user_delete(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return {"message": "User deleted"}


@user_router.post("/users", response_model=UserSchema)
def user_post(user: UserCreate, db:Session = Depends(get_db)):
    return create_user(db, user)

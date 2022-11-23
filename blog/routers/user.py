from fastapi import APIRouter, Depends
from blog import database, schemas
from sqlalchemy.orm import Session
from blog.repository import user

router = APIRouter(
    prefix='/user',
    tags=['Users']
)

@router.post('/', response_model=schemas.ShowUser, status_code=201)
def create_user(request: schemas.User, db: Session = Depends(database.get_db)):
    return user.create(request, db)

@router.get('/{id}', response_model=schemas.ShowUser)
def show_user(id:int, db: Session=Depends(database.get_db)):
    return user.show(id, db)
from fastapi import APIRouter, HTTPException, status, Depends
from schemas.user import UserCreate, UserSignin
from sqlalchemy.orm import Session
from repository.database import get_db
from core.dependencies import get_current_user
from services.user import register, authenticate
from exceptions.user import UserAlreadyExistsException, UserNotFoundException, InvalidPasswordException
from schemas.user import Token

user_router = APIRouter(tags=["User"])

# 회원가입(회원 생성)
@user_router.post("/signup")
async def post_new_user(data:UserCreate, db:Session = Depends(get_db)):
    
    try:
        user = register(db=db, data=data)
    except UserAlreadyExistsException:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="사용중인 email 입니다."
        )

    return {"message":f"{user.user_id}등록 성공"}


# 로그인 
@user_router.post("/signin", response_model=Token)
async def sign_user(data:UserSignin, db: Session=Depends(get_db)):

    try:
        token = authenticate(data=data, db=db)
    except UserNotFoundException:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="이메일과 비밀번호를 확인해 주세요"
        )

    except InvalidPasswordException:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="이메일과 비밀번호를 확인해 주세요"
        )

    return token
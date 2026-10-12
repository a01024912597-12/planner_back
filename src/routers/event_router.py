from fastapi import APIRouter, HTTPException, status, Depends
from schemas.event import EventItem, EventCreate, EventResponse
from services.event import add_event, find_events_by_user_id, delete_user_event
from sqlalchemy.orm import Session
from repository.database import get_db
from repository.models.user import User
from core.dependencies import get_current_user
from exceptions.event import EventNotFoundException
from exceptions.user import UserCreditialsException


event_router = APIRouter(tags=["Events"])

events = []




# 특정 이벤트 조회
# http://127.0.0.1:8000/evnet/1 + get
@event_router.get("/{id}", response_model=EventItem)
async def get_event(id:int):
    for event in events:
        if event.id == id:
            return event
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="이벤트가 없습니다.")


# 전체 이벤트 조회
@event_router.get("/", response_model=EventResponse)
async def get_event(db:Session=Depends(get_db), current_user:User=Depends(get_current_user)):
    events = find_events_by_user_id(db=db, current_user=current_user)
    return {"items":events}

# 이벤트 추가
# http://127.0.0.1:8000/evnet/new + post
@event_router.post("/new", response_model=EventItem)
async def post_event(data:EventCreate, db:Session=Depends(get_db), current_user:User=Depends(get_current_user)):
    event = add_event(db=db,data=data,current_user=current_user)

    return event

# 특정 이벤트 삭제
# http://127.0.0.1:8000/evnet/1 + delete 
# 특정 이벤트 삭제
@event_router.delete("/{id}", response_model=dict)
async def delete_event(
    id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    try:
        delete_user_event(
            db=db,
            id=id,
            current_user=current_user
        )
    except EventNotFoundException:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="제거할 이벤트가 없습니다."
        )
    except UserCreditialsException:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="삭제할 권한이 없습니다."
        )

    return {"message": f"event {id}번 삭제"}

# 전체 이벤트 삭제
# http://127.0.0.1:8000/evnet/ + delete
@event_router.delete("/")
async def delete_all_events():
    events.clear()
    return {"message":"모든 Event 삭제 성공"}
from pydantic import BaseModel
from typing import List

class EventCreate(BaseModel):
    title: str
    image: str
    description: str
    tags:List[str]
    location:str

    model_config={
        "json_schema_extra":{
            "examples":[
                {
                    "title":"이벤트 제목",
                    "image":"이벤트 이미지 URL 예) https://linktomyimage.com/image.png",
                    "description":"이벤트 설명",
                    "tags": ["pyhhon", "fastapi", "book", "launch"],
                    "location":"이벤트 장소",

                }
            ]
        }
    }
    
class Event(EventCreate):
    id:int
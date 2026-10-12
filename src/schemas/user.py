from pydantic import BaseModel
from typing import List,Optional

# 사용자가 생성한 이벤트
class User(BaseModel):
    email: str  
    password: str  
    events: Optional[List[str]]      

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "email": "fastapi@gmail.com",
                    "password": "strong!!!",                  
                    "events": [],                   
                }
            ]
        }
    }
class UserCreate(BaseModel):
    email:str
    password: str

class UserSignin(BaseModel):
    email: str  
    password: str          

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "email": "fastapi@gmail.com",
                    "password": "strong!!!",                
                               
                }
            ]
        }
    }



class Token(BaseModel):
    access_token:str
    token_type:str="bearer"
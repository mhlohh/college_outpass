from pydantic import BaseModel

class OutPass(BaseModel):
    name:str
    course:str
    id:str
    reason:str
    date:str
    inside:str
    outside:str

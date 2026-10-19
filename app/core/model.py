from pydantic import BaseModel

# Describe the information a student must provide for an outpass.
# FastAPI uses this model to validate incoming JSON and parse it into Python data.
class OutPass(BaseModel):
    name:str
    course:str
    id:str
    reason:str
    date:str
    outside:str
    inside:str

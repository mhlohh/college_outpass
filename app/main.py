from fastapi import FastAPI, HTTPException, status
from app.model import OutPass
app = FastAPI()

lists = {

    "4122341": OutPass(
        name="Muhsil NR",
        course="Btech AI/ML",
        id= "4122341",
        reason="Cycling",
        date="02/08/2026",
        inside="6:30",
        outside="4:30")
}

@app.get("/outpass")
def outpass():
    return lists

@app.get("/outpass/{id}")
def get_outpass_register(id:str):
    if id not in lists:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with Registration ID {id} does not exist"
        )
    else:
        return lists[id]

@app.post("/outpass")
def add_outpass(outpass:OutPass):
    lists[outpass.id] = outpass
    return outpass

@app.put("/outpass/{id}")
def update_outpass(outpass:OutPass, id:str):
    if id not in lists:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with Register ID {id} does not exist"
        )
    else:
        outpass.id = id
        lists[id] = outpass

from fastapi import FastAPI, HTTPException, status
from app.core.data_loader import all_outpass_data,outpass_id_data,add_outpass_data
from app.core.model import OutPass
import csv
import os
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
    return all_outpass_data()

@app.get("/outpass/{id}")
def get_outpass_(id:str):
    return outpass_id_data(id)
  
@app.post("/outpass")
def add_outpass(outpass:OutPass):
    return add_outpass_data(outpass)

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

@app.delete("/outpass/{id}")
def delete_outpass(id):
    if id in lists:
        del lists[id]

    return "Deleted Sucessfully"
        

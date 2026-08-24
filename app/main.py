from fastapi import FastAPI, HTTPException, status
from app.core.data_loader import (
    all_outpass_data,
    outpass_id_data,
    add_outpass_data,
    update_outpass_data,
    delete_outpass_data,
)
from app.core.model import OutPass
import csv
import os

app = FastAPI()


@app.get("/outpass")
def outpass():
    return all_outpass_data()


@app.get("/outpass/{id}")
def get_outpass_(id: str):
    return outpass_id_data(id)


@app.post("/outpass")
def add_outpass(outpass: OutPass):
    return add_outpass_data(outpass)


@app.put("/outpass/{id}")
def update_outpass(outpass: OutPass, id: str):
    update_outpass_data(outpass, id)


@app.delete("/outpass/{id}")
def delete_outpass(id):
    delete_outpass_data(id)

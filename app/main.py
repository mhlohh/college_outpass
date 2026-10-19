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

# Create the FastAPI application that serves the outpass endpoints.
app = FastAPI()


@app.get("/outpass")
def outpass():
    """Return all outpasses currently held by the data layer."""
    return all_outpass_data()


@app.get("/outpass/{id}")
def get_outpass_(id: str):
    """Return the outpass matching the requested college ID."""
    return outpass_id_data(id)


@app.post("/outpass")
def add_outpass(outpass: OutPass):
    """Validate and add a new outpass submitted as JSON."""
    return add_outpass_data(outpass)


@app.put("/outpass/{id}")
def update_outpass(outpass: OutPass, id: str):
    """Update the outpass identified by the URL ID using the submitted data."""
    update_outpass_data(outpass, id)


@app.delete("/outpass/{id}")
def delete_outpass(id):
    """Delete the outpass identified by the URL ID."""
    delete_outpass_data(id)

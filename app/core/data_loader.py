from app.core.data_config import(
    intialize_data_set,
    file_path
)
import os
import csv
from fastapi import FastAPI, HTTPException, status


outpass_dict = {}
dict_list = []
#load csv as dictionary
if os.path.exists(file_path):
    with open(file_path,"r") as file:
        reader = csv.DictReader(file)
        dict_list = list(reader)
    for item in dict_list:
        outpass_dict[item["id"]] = item
        print(outpass_dict)
else:
    print("WARNING:    The dataset is not Intilaized ❌")
    intialize_data_set()
    print("INFO:    The dataset is intialized ☑️")

#convert dict_list to id value pair

#Load entire contents in dataset
def all_outpass():
    return outpass_dict

#Load specific Outpass
def outpass_id(id):
    id = str(id)
    if id in outpass_dict:
        return outpass_dict[id]
    else:
        print("WARNING:  Item not found ❌")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Item not found"
        )
        
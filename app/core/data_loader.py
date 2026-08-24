from app.core.data_config import intialize_data_set, file_path, field_names
from fastapi import HTTPException, status
from app.core.model import OutPass
import os
import csv

outpass_dict = {}
dict_list = []
# load csv as dictionary
if os.path.exists(file_path):
    with open(file_path, "r") as file:
        reader = csv.DictReader(file)
        dict_list = list(reader)
    for item in dict_list:
        outpass_dict[item["id"]] = item

else:
    print("WARNING:    The dataset is not Intilaized ❌")
    intialize_data_set()
    print("INFO:    The dataset is intialized ☑️")

# convert dict_list to id value pair


# Load entire contents in dataset
def all_outpass_data():
    print(list(outpass_dict.values()))
    data = list(outpass_dict.values())
    for value in data:
        print(value)
    return outpass_dict


# Load specific Outpass by iud
def outpass_id_data(id):
    id = str(id)
    if id in outpass_dict:
        return outpass_dict[id]
    else:
        print("WARNING:  Item not found ❌")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item not found"
        )


# Add an Outpass
def add_outpass_data(outpass: OutPass):
    print(f"INFO:   Outpass Aded Sucessfuly id:{outpass.id} ☑️")
    outpass_dict[outpass.id] = outpass
    data = dict(outpass)
    with open(file_path, "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=field_names)
        writer.writerow(data)
    return outpass


# update outpass
def update_outpass_data(outpass, id):
    id = str(id)
    if id not in outpass_dict:
        print("INFO:     Not found to update")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with Register ID {id} not Found!",
        )

    else:
        outpass_dict[id] = outpass
        data = [dict(value) for value in outpass_dict.values()]
        with open(file_path, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=field_names)
            writer.writeheader()
            writer.writerows(data)
            print(f"INFO:    UPdated Sucessfully id: {id} ☑️")

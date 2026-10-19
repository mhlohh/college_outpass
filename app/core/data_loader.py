from app.core.data_config import intialize_data_set, file_path, field_names
from fastapi import HTTPException, status
from app.core.model import OutPass
import os
import csv

# Keep outpasses in memory so lookups by college ID are fast on average.
outpass_dict = {}
dict_list = []
# Load saved rows at startup and index each one by its college ID.
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

def all_outpass_data():
    """Return all currently stored outpasses, keyed by college ID."""
    data = list(outpass_dict.values())
    for value in data:
        print(value)
    return outpass_dict


# Load specific Outpass by id
def outpass_id_data(id):
    """Find one outpass by college ID, or return an HTTP 404 error."""
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
    """Add a new outpass to memory and append its row to the CSV file.

    College ID is the dictionary key, so an existing ID cannot be added twice.
    """
    if outpass.id not in outpass_dict:
        print(f"INFO:   Outpass Aded Sucessfuly id:{outpass.id} ☑️")
        outpass_dict[outpass.id] = outpass
        data = dict(outpass)
        with open(file_path, "a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=field_names)
            writer.writerow(data)
        return outpass
    else:
        print("WARNING:  ID already exist")
        raise HTTPException(
            detail=f"Id {outpass.id} already exist"
        )


# update outpass
def update_outpass_data(outpass, id):
    """Replace an existing outpass and rewrite the CSV with the updated data."""
    id = str(id)
    if id not in outpass_dict:
        print("INFO:     Not found to update")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with Register ID {id} not Found!",
        )

    else:
        outpass_dict.pop(id)
        outpass_dict[outpass.id] = outpass
        data = [dict(value) for value in outpass_dict.values()]
        with open(file_path, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=field_names)
            writer.writeheader()
            writer.writerows(data)
            print(f"INFO:     Updated Sucessfully id: {id} ☑️")


# Delete an outpass
def delete_outpass_data(id):
    """Remove an outpass from memory and rewrite the CSV without that row."""
    if id in outpass_dict:
        del outpass_dict[id]
        data = [dict(value) for value in outpass_dict.values()]
        with open(file_path, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=field_names)
            writer.writeheader()
            writer.writerows(data)
            print(f"INFO: Deleted Sucessfully id: {id} ☑️")
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item not found"
        )

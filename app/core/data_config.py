from app.core.model import OutPass
import csv
import os

# Use the model's fields as CSV columns so stored rows match the API data shape.
field_names = list(OutPass.model_fields.keys())

file_name = "student_outpass"

file_path = f"data/{file_name}.csv"


def intialize_data_set(field_names=field_names):
    """Create the CSV file with a header row when it does not already exist."""
    if os.path.exists(file_path):
        print("File already exist!")
    else:
        with open(file_path, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=field_names)
            writer.writeheader()

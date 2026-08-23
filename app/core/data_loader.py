from dataclasses import dataclass, asdict
from model import OutPass
import csv

@dataclass
class User:
    username: str
    email: str
    active: bool

# Create an instance
user_profile = User(username="johndoe", email="john@example.com", active=True)

# Convert to dictionary
user_dict = asdict(user_profile)
userProfile = [user_dict]
print(user_dict)
# Output: {'username': 'johndoe', 'email': 'john@example.com', 'active': True}

# CSV file name
csv_filename = "cars.csv"

# Define the field names (headers)
fieldnames = ["username", "email", "active"]

# Writing to CSV
with open(csv_filename, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()  # Write header row
    writer.writerows(userProfile)  # Write data rows
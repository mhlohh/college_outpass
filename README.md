# College Outpass

## The Problem

Students currently use a paper outpass to leave campus. The slip needs signatures
from four administrators, so a student has to find each person and wait. This can
take a long time, especially during an emergency.

## The Solution

Build a backend that stores outpass requests and makes them available to
administrators on their phones. The aim is to let administrators review and
approve requests without the student having to visit each office. Sending live
updates to administrator devices is part of the intended system; the current
backend is an early step focused on storing and managing outpasses.

## Design Decisions

- **FastAPI** is used to create the backend API. It is a Python framework, and
  Python is already familiar to the project author.
- **Pydantic** defines the shape of an outpass and validates request data. It
  also turns incoming JSON into a Python `OutPass` model.
- **CSV** is the current persistent store. It keeps the data simple to inspect
  while the first version is being built.
- **A Python dictionary** holds the loaded outpasses in memory, indexed by the
  student's college ID. This makes an ID lookup fast on average and gives the
  application a direct way to find a record to update or delete. The dictionary
  is rebuilt from the CSV when the backend starts.

## Outpass Data

The `OutPass` model represents the details collected from the student, similar
to the fields on the paper slip: name, course, college ID, reason, date, and the
planned times outside and back inside.

## Current API and Data Flow

The API provides the basic create, read, update, and delete operations (CRUD):

- `GET /outpass` returns all outpasses.
- `GET /outpass/{id}` finds one outpass by college ID.
- `POST /outpass` adds an outpass, unless that ID already exists.
- `PUT /outpass/{id}` updates an existing outpass.
- `DELETE /outpass/{id}` removes an outpass.

The route functions in `app/main.py` pass requests to `app/core/data_loader.py`.
That module uses the in-memory dictionary for lookups and writes changes to
`data/student_outpass.csv` so records can be loaded again after a restart.

## Build and Setup
```bash
cd college_outpass
```

```bash
mkdir data
```

```bash
pip install -r requirements.txt
```
## Run the Backend
```bash
uvicorn app.main:app --reload
```

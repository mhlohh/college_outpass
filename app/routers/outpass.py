from fastapi import APIRouter,HTTPException

router = APIRouter(prefix="/insights", tags=["insights"])

@router.get("/outpass")
def outpass():
    return "Hello"

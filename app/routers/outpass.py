from fastapi import APIRouter,HTTPException

# Group insight-related endpoints under a shared URL prefix and API tag.
router = APIRouter(prefix="/insights", tags=["insights"])

@router.get("/outpass")
def outpass():
    """Simple placeholder endpoint for an outpass insight response."""
    return "Hello"

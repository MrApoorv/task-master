from fastapi import APIRouter

router = APIRouter(tags=["greet"])

@router.get('/signup')
def signup():
    return "signing up"
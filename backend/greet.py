from fastapi import APIRouter

router = APIRouter(tags=["greet"])

@router.get('/')
def greet():
    return "hello 2k26"
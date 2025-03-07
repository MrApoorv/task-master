from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import greet, todos, db_tester
app = FastAPI()
#instance of FastAPI class
origins = ['http://localhost:3000']
app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["GET","POST",'PUT', 'DELETE' , 'UPDATE'],
    allow_headers=["*"]
)    

app.include_router(greet.router)
app.include_router(todos.router)



#pip install fastapi
#pip install uvicorn
#pip freeze
#env1/Scripta/Activate
#uvicorn  - to run  server ->  uvicorn main:app --reload port {port on which you wannt to run}
# --reload : changes are made automatically
# --port 9000 : change port
# @app.get('/')
# def greet():
#     return '2k23'
# @app.get('/greet/{name}')
# def greetByName(name: str):
#     return f'Hello {name}'
# /docs 
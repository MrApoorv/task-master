from typing import List, Optional
from fastapi import FastAPI,HTTPException,status,Query
app = FastAPI()

todos = [{
    "title": "Wakeup",
    "description": "Wake up at 7am",
    "status": "done"
},{
    "title": "Class",
    "description": "Class at 5:30pm",
    "status": "Progress"
},{
    "title": "Study",
    "description": "Study at 9:30pm",
    "status": "yet to be done"
}
]
#get all todos
@app.get('/api/v1/todos')
def getAllTodos(limit: Optional[int] = Query(1), offset : Optional[int] = Query(0)) -> List[dict]:
    start_idx = int(offset)
    end_idx = start_idx + int(limit)
    return todos[start_idx : end_idx]

#get specific todo
@app.get('/api/v1/todos/{title}',status_code=status.HTTP_200_OK)
def getTodo(title: str)-> dict:
    for todo in todos:
        if todo['title'] == title:
            return todo
    raise HTTPException(status.HTTP_404_NOT_FOUND, detail = f"todo not found with title {title}");

#get todo by status
@app.get('/api/v1/todos/status/{status}',status_code=status.HTTP_200_OK)
def get_todo_by_status(status:str) -> List[dict]:
    all = []
    for todo in todos:
        if todo['status'] == status:
            all.append(todo)
    return all

#constraint check
def check_todo(title):
    for todo in todos:
        if title == todo['title']:
            return True
    return False

##create todo and enforce that title is unique
@app.post('/api/v1/createTodo',status_code=status.HTTP_201_CREATED) #return this status if there is no other status returned
def createTodo(todo: dict) -> bool:
    if check_todo(todo['title']):
        message = f"Cannot add todo as the title {todo['title']} already exists"
        raise HTTPException(status.HTTP_409_CONFLICT,message)
    todos.append(todo)
    return True

    
@app.delete('/api/v1/deleteTodo/{title}',status_code=status.HTTP_200_OK)
def deleteTodo(title: str) -> bool:
    for todo in todos:
        if todo['title'] == title:
            todos.remove(todo)
            return True
    raise HTTPException(status.HTTP_400_BAD_REQUEST,detail = f"No todo found with title {title}")
    
@app.put('/api/v1/updateTodo',status_code=status.HTTP_200_OK)
def updateTodo(payload:dict) -> bool:
    updateidx= -1
    for idx,todo in enumerate(todos):
        if todo['title'] == payload['title']:
            updateidx = idx
    if updateidx == -1 :
        raise HTTPException(status.HTTP_404_NOT_FOUND,detail=f"No todo exists with the title {payload['title']}")           

    todos[updateidx]['status'] = payload['status']
    todos[updateidx]['description'] = payload['description'] 
    return True   



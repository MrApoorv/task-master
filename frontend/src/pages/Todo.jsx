import React from 'react'
import axios from 'axios';
import { useEffect, useState } from 'react';
import TodoItem from '../components/TodoItem';
import IonIcon from '@reacticons/ionicons'

const Todo = () => {
  const [todos, setTodos] = useState([]);

  useEffect(()=>{
    axios.get('http://127.0.0.1:8000/api/v1/todos')
      .then((res) => { 
        setTodos(res.data) 
        console.log(res.data);
      })},[])

  const addTodo = (e) =>{
    e.preventDefault();
    const todoItem = {'title':e.target[0].value,'des':e.target[1].value,'status':e.target[2].value}
    axios.post('http://localhost:8000/api/v1/todos/createTodo',todoItem)
    .then((res) => {
      console.log(res.data);
      setTodos([...todos, todoItem]);
      e.target[0].value = '';
      e.target[1].value = '';
      e.target[2].value = '';
      })
  }
  const deleteTodo = (idx) =>{
    const todoItem = todos[idx];
    axios.delete(`http://127.0.0.1:8000/api/v1/todos/delete-by-title/${todoItem.title}`)
     .then((res)=>{
      console.log(res.data);
      todos.splice(idx,1);
      setTodos(todos);
     })
  }
  return (
    <div className="App">
      <form className='Add_Todo' onSubmit={(e)=> addTodo(e)}>
        <input type="text" name="title" id='title' placeholder='Enter Title'/>
        <input type="text" name="desc" id='desc' placeholder='Enter Description'/>
        <input type="text" name="status" id='status' placeholder='Enter Status'/>
        <button type='submit' id='add-todo-btn'>
          <IonIcon name='add'></IonIcon>
        </button>
      </form>
      <h1 id='heading'>ToDo List</h1>
      <div className="divider"></div>
      <div className="todoList">
      { 
        todos.map((todo,idx) => <TodoItem key={todo.title} idx={idx} title = {todo.title}  
        desc = {todo.des} status = {todo.status} deleteTodo={deleteTodo}/> )
       }
      </div>
    </div>
  );
}

export default Todo
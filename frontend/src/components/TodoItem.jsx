import React from 'react';
import './TodoItem.css';
import IonIcon from '@reacticons/ionicons'


function TodoItem(props) {
  let title = props.title;
  let description = props.desc || "default description";
  let status = props.status;
  let createAt = props.createAt;
  // let borderColor = props.borderColor;

  return (
    // <div className='TodoItem' style={{ borderTop: `6px solid ${borderColor}` }} >
    <div className='TodoItem' >
      <div className="todo-header">
        <h2>{title}</h2>
        <button id='delete-todo-btn' onClick={()=> props.deleteTodo(props.idx)}>
          <IonIcon id='delete-todo-img' name='trash'></IonIcon>
        </button>
      </div>
      <p>{description}</p>
      <div className='stats'></div>
      <p className='para'>{status}</p>
      <p>created at: {createAt}</p>
    </div>
  )
}

export default TodoItem
import React from 'react'
import { useState } from 'react'
const Counter = () => {
    const [count, setCount] = useState(0);
    const increment = () =>{
        setCount(count+1);
    }
  return (
    <>
        {count}
        <button onClick={increment}>Increment</button>
    </>
  )
}

export default Counter
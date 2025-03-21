import React from 'react'
import './NavBar.css'
import { Link } from 'react-router-dom'

const NavBar = () => {
  return (
    <div className='NavBar'>
        <Link to="/"> Home </Link>
        <Link to="/about"> About </Link>
        <Link to="/login"> Login </Link>
        <Link to="/signup"> Sign up</Link>
    </div>
  )
}

export default NavBar
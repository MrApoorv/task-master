import './App.css';
import About from './pages/About';
import Login from './pages/Login';
import SignUp from './pages/SignUp';
import Todo from './pages/Todo';
import Error from './pages/Error';

import  {BrowserRouter, Route, Routes } from 'react-router-dom'

function App() {
  return (
    <BrowserRouter>
    <Routes>
      <Route exact path='/' element = { <Todo/> }></Route>
      <Route exact path='/about' element = { <About/> }></Route>
      <Route exact path='/login' element = { <Login/> }></Route>
      <Route exact path='/signup' element = { <SignUp/> }></Route>
      <Route exact path='*' element = { <Error/> }></Route>
    </Routes>
    </BrowserRouter>
  );
}

export default App;

import React from 'react'
import { Routes,Route} from 'react-router-dom'
import Home from './pages/Home/Home'
import Auth from './pages/Auth/Auth'
import Questions from './pages/Questions/Questions'
import AskQuestion from './pages/AskQuestion/AskQuestion'
const AllRoutes = () => {
  return (
    <div>
      <Routes>
        <Route exact path='/' element={<Home />}></Route>
        <Route exact path='/Auth' element={<Auth />}></Route>
        <Route exact path='/Questions' element={<Questions />}></Route>
        <Route exact path='/AskQuestion' element={<AskQuestion />}></Route>
      </Routes>
    </div>
  )
}

export default AllRoutes

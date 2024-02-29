import React from 'react'
import { Link } from 'react-router-dom'
import logo from '../../assets/logo.jpeg'
import search from '../../assets/magnifying-glass-solid.svg'
import Avatar from '../../components/Avatar/Avatar'
import Button from '../../components/Button/Button'
import './Navbar.css'
const Navbar = () => {

  var user = null //This is to store the user deatils after authentication

  return (

    

    <nav>
        <div className='main-nav'>
            <Link to='/' className='nav-item nav-logo'>
                <img className='logo' src={logo} alt="logo"/> 
            </Link>
            <Link to='/' className='nav-item nav-btn'>About</Link>
            <Link to='/' className='nav-item nav-btn'>Products</Link> 
            <Link to='/' className='nav-item nav-btn'>For Teams</Link> 
          <form action="">
            <input type="text" placeholder='Search...' />
            <img className='search-icon' src={search} alt="search" width="18"/>
          </form>

          {user === null ?
          
            <Link to='/Auth' className='nav-item nav-links'>Log in</Link> :
            
            <>
                <Avatar backgroundColor='#009dff' px="10px" py="7px" borderRadius="50%" color="white" width="30px" height="25px" ><Link to='/user' style={{color:"white" , textDecoration:"none" , width:"30px"}}>P</Link></Avatar>
                {/* // first letter of the user */}
                <button className='nav-item nav-links'>Log out</button>        
            </>

          }
        </div>
        
    </nav>
  )
}

export default Navbar

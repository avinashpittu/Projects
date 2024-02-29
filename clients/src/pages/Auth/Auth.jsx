import React, { useState, useEffect } from 'react'
import './Auth.css'
import icon from '../../assets/icon.png'
import AboutAuth from './AboutAuth'
const Auth = () => {

  const [isSignup, setisSignup] = useState(false)
  const handleSwitch = () =>{
    setisSignup(!isSignup)
  } 

  return (
    <div>
      <section class='auth-section'>
        {isSignup && <AboutAuth/>}
        <div className='auth-container-2'>
            {!isSignup && <img src={icon} alt='stack overflow' className='login-logo' style={{width:"50px",height:"50px"}}/>}
            <form action="">
              {
                isSignup && (
                  <label htmlFor="name">
                    <h4>Display Name</h4>
                    <input type="text" id='name' name='name'/>
                  </label>
                )
              }

              <label htmlFor="email">
                <h4>Email</h4>
                <input type="email" name='email' id='email' />

              </label>
              <label htmlFor="password">
                
                <div style={{display: "flex", justifyContent: "space-between"}}>
                <h4>Password</h4>
                { !isSignup && <h4 style={{color: "#007ac6", fontSize:"13px"}}>forgot password?</h4>}
                {/* this is how we write conditon in react without if-else using &&- if its true then next line will execute*/}
                </div>
                <input type="password" name='password' id='password' />
                {/* <br /> */}
                { isSignup && <p style={{color: "#666767", fontSize:"13px"}}>Passwords must contain at least eight <br /> characters, including at least 1 letter and 1 <br /> number.</p>}
              </label>
              {
                isSignup && (
                  <label htmlFor="check">
                    <input type="checkbox" id='check'/>
                    <p >Opt-in to receive occasional, <br /> product updates, user research invitations, <br /> company announcements, and digest</p>
                  </label>
                )
              }
              <button type='submit' className='auth-btn'>{isSignup ?'Sign up': 'Log in'}</button>
              {
                isSignup && (
                  <p style={{color: "#666767", fontSize:"13px"}}>
                    By clicking "sign up", yu agree to our 
                    <span style={{color: "#007ac6"}}> terms of <br /> service</span>, 
                    <span style={{color: "#007ac6"}}> privacy policy</span> and 
                    <span style={{color: "#007ac6"}}> cookie policy</span>  
                  </p>
                )
              }
            </form>
            <p>
              {isSignup ? 'Already have an account?' : "Don't have an account?"}
              <button type='button' className='handle-switch-btn' onClick={handleSwitch}>{ isSignup ? "Log in" : "sign up"}</button>
            </p>
            {/* <p>
              {isSignup ? 'already have an account? ' : "Don't have an account?}
              <button type='button' className='handle-switch-btn'>{ isSignup ? "Log in" : "Sign up"}</button>
            </p> */}
        </div>
      </section>
    </div>
  )
}

export default Auth

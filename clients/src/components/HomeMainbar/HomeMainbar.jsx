import React from 'react'
import {Link, useLocation, useNavigate } from 'react-router-dom'
import QuestionList from './QuestionList'
import './HomeMainbar.css'

const HomeMainbar = () => {
    var questionsList = [{
        id: 1,
        votes: 3,
        noOfAnswers: 2,
        questionTitle: "What is a function?",
        questionBody: "It meant to be",
        questionTags:["java","react js","node js","mongodb"],
        userPosted: 'Praneeth',
        askedOn: 'jan 1'
    },{
        id: 2,
        votes: 0,
        noOfAnswers: 0,
        questionTitle: "What is a function?",
        questionBody: "It meant to be",
        questionTags:["javascript","R","python"],
        userPosted: 'Gowri',
        askedOn: 'jan 1'
    },{
        id: 3,
        votes: 1,
        noOfAnswers: 0,
        questionTitle: "What is a function?",
        questionBody: "It meant to be",
        questionTags:["javascript","R","python"],
        userPosted: 'Pragun',
        askedOn: 'jan 1'
    }]
    const user = 1;
    const navigate = useNavigate()
    // const redirect = () => {
        
    // }
    const checkAuth = () =>{
        if (user === null){
            alert("Login or signup to ask question")
            navigate('/Auth')
        }
        else{
            navigate('/AskQuestion')
        }
    }
    const Location = useLocation()
  return (
    <div className='main-bar'>
        <div className='main-bar-header'>
            {
                Location.pathname === '/' ? <h1>Top Questions</h1> : <h1>All Questions</h1>

            }
            <button onClick={checkAuth} className='ask-btn'>Ask Question</button>
            </div>
            <div >
                {
                    questionsList === null?
                    <h1>Loading...</h1> :
                    <>
                        <p>{ questionsList.length } questions</p>
                        <QuestionList questionsList={questionsList} />
                    </>
                }
            </div>
        
      
    </div>
  )
}

export default HomeMainbar

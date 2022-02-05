import React from 'react'
import { useState} from 'react';
import {Link} from 'react-router-dom'
import Card from '../components/ui/Card';
import axiosInstance from './../axiosApi'
import classes from './Signup.module.css'
import { useHistory } from 'react-router';
/*
Page where user can login or go to SignUp page
*/

export default function LoginPage(props) {
    const [email,setEmail] = useState('');
    const [password,setPassword] = useState('');
    const history = useHistory();


    /*
    updates password state on change
    */
    function handleChangePassword(event) {
        setPassword(event.target.value)
        console.log(password);
    }

    /*
    updates email state on change
    */
    function handleChangeemail(event) {
        setEmail(event.target.value)
        console.log(email);
    }

    /*
    sends a user information to the server if the user already exist sends back a refresg token to confirm user exist
    and lets user log in to the website
    */
    function handleSubmit(event) {
        event.preventDefault();
        try{
            axiosInstance.post('https://buddyguy-api.aswang.co/api/token/obtain/', {
                email: email,
                password: password
            })
            .then(response =>{
            console.log(response);
            console.log(response.data.access);
            console.log(response.data.refresh);
            axiosInstance.defaults.headers['Authorization'] = "JWT " + response.data.access;
            localStorage.setItem('access_token', response.data.access);
            localStorage.setItem('refresh_token', response.data.refresh);
            history.push('/home');
            return response.data;
            });
        }
        catch(error){
            throw error;
        }
    }

    /*
    HTML for Login Page
    */
    return (
        <div>
            <header className={classes.header}>
                <div className= {classes.logo}>
                    {props.title}
                </div>
            </header>
            <Card>
                <form onSubmit={handleSubmit} className={classes.form}>
                    <div className={classes.control}>
                        <label>
                        Email:
                        <input name="email" type="text" value={email} onChange={handleChangeemail} required/>
                    </label>
                    </div>
                    
                    
                    <div className={classes.control}>
                        <label>
                        Password:
                        <input name="password" type="password" value={password} onChange={handleChangePassword} required/>
                    </label>
                    </div>

                    <div className={classes.actions}>
                        <button>Login</button>
                    </div>

                </form>
            </Card>
            <div>
                <Link to='/signUp'><button>SignUp</button></Link>
            </div>
        </div>
        
    );
}
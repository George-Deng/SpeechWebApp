import React from "react";
import { useState} from 'react';
import Card from "../components/ui/Card";
import classes from './Signup.module.css'
import ConsentModal from "../components/consentModals/ConsentModal";
import Backdrop from "../components/Modal/Backdrop";
import { useHistory } from "react-router";
/*
Page where user can SignUp 
*/

export default function SignupPage(props) {
    const [email,setEmail] = useState('');
    const [password,setPassword] = useState('');
    const [userType,setUserType] = useState("Patient");
    const [userNumber,setUserNumber] = useState(1);
    const [errorData,setErrorData] = useState('');
    const[modalConsent, setModalConsentIsOpen] = useState(false);
    const history = useHistory();

    /*
    opens up modal with consent form
    */
    function resultHandler(){
        setModalConsentIsOpen(true);
    }

    /*
    closes modal with consent form
    */
    function closeModalHandler(){
        setModalConsentIsOpen(false);
    }

    /*
    changes password state on change
    */
    function handleChangePassword(event) {
        setPassword(event.target.value)
        console.log(password);
    }

    /*
    changes email state on change
    */
    function handleChangeEmail(event) {
        setEmail(event.target.value)
        console.log(email);
    }

    /*
    sends new user information back to server to create a new user
    */
    function handleSubmit(event) {
        event.preventDefault();
        var axios = require('axios');
        var FormData = require('form-data');
        var data = new FormData();
        data.append('email', email);
        data.append('password', password);
        data.append('password2', password);
        data.append('user_type', userNumber);

        var config = {
        method: 'post',
        url: 'https://buddyguy-api.aswang.co/api/user/create/',
        data : data
        };

        axios(config)
        .then(function (response) {
        console.log(JSON.stringify(response.data));
        history.push('/');
        })
        .catch(function (error) {
        console.log(error);
        setErrorData(error);
        });
        // try {
        //     axios.post('https://buddyguy-api.aswang.co/api/user/create/', {
        //         user_type: userNumber,
        //         email: email,
        //         password: password,
        //         password2: password
        //     }).then(response=>{
        //         console.log(response);
        //         history.push('/');
        //         return response;
        //     })
            
        // } 
        // catch (error) {
        //      console.log(error.stack);
        //      setErrorData(error.response.data)
        // }
    }

    /*
    setting user type
    */
    function handleChangeType(event) {
        event.preventDefault();
        setUserType(event.target.value);
        if(event.target.value === "Patient"){
            setUserNumber(1); // patient
        } else{
            setUserNumber(2); // doctor
        }
        console.log(userType);
       
    }

/*
HTML for SignUp page
*/
    return (
        <div >
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
                            <input name="email" type="text" value={email} onChange={handleChangeEmail} required/>
                            { errorData.email ? errorData.email : ''}
                        </label>
                    </div>

                    <div className={classes.control}>
                        <label>
                            Password:
                            <input name="password" type="password" value={password} onChange={handleChangePassword} required/>
                            { errorData.password ? errorData.password : ''}
                        </label>
                    </div>

                    <div className={classes.control}>
                        
                        <select value = {userType} onChange={handleChangeType}>
                            <option value= "Doctor">Doctor</option>
                            <option value="Patient">Patient</option>
                        </select>
                    </div>
                  
                    <div>
                        <p onClick={resultHandler} style = {{ color: 'blue', cursor: 'pointer' }}> <u>Read Terms and Conditions </u></p>
                        <input type="checkbox" id="consent"  required/>
                        <label htmlFor="consent">Accept Terms and Conditions</label>
                    </div>
                    <div className={classes.actions}>
                        <button>Submit</button>
                    </div>
                </form>
                { modalConsent && <ConsentModal/>}
                { (modalConsent) && <Backdrop onClick={closeModalHandler}/>}
            </Card>
        </div>
    );
}



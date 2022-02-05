
import {useState} from 'react';
import axiosInstance from './../axiosApi'
import {useEffect} from 'react';
import React from 'react'



export default function Hello() {
    const [message,setMessage] = useState('');


    async function  getMessage(){
        try {
            axiosInstance.get('/hello').then(response=>{
                const message = response.data.hello;
                setMessage(message);
                return message;
            });
            
        }
        catch(error){
            console.log("Error: ", JSON.stringify(error, null, 4));
            throw error;
        }
    }
    
    useEffect (() =>{
       // It's not the most straightforward thing to run an async method in componentDidMount
    
        // Version 1 - no async: Console.log will output something undefined.
        const messageData1 = getMessage();
        console.log("messageData1: ", JSON.stringify(messageData1, null, 4));
    }) 
    
    // function componentDidMount(){
    //     // It's not the most straightforward thing to run an async method in componentDidMount
    
    //     // Version 1 - no async: Console.log will output something undefined.
    //     const messageData1 = getMessage();
    //     console.log("messageData1: ", JSON.stringify(messageData1, null, 4));
    // }


    return (
        <div>
            <p>{message}</p>
        </div>
    )
}

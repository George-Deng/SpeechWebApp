import React from 'react'
import { useState } from 'react';
import Modal from '../Modal/Modal';
import Card from '../ui/Card';
import classes from './AnnotateModal.module.css'
import axios from 'axios';
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

/*
takes in annotation from user and sends an object containing all information to server 
to be saved for the currently selected upload
*/
export default function AnnotateModal(props) {
    const [startTime, setStartTime] = React.useState("0:00");
    const [displayStartTime, setDisplayStartTime] = React.useState("0:00");

    const [endTime, setEndTime] = React.useState("0:00");
    const [displayEndTime, setDisplayEndTime] = React.useState("0:00");

    const [annotations,setAnnotations] = useState('');
    const notifyFileUploaded =  () =>toast("Annotation was successfuly uploaded!");
    const notifyBadTime =  () =>toast("EndTime must be later than StartTime ");
    let URL ='https://buddyguy-api.aswang.co/api/annotations/' + props.id
    console.log(URL)

   /*
    updates end time state on change
   */
    function handleChangeEndTime(event) {
        setDisplayEndTime(event.target.value);
        console.log("Onchange " + displayEndTime);
    }

     /*
    unhighlights end time when not clicked
    */
    function onBlurEndTime(event){
        const value = event.target.value;
        const seconds = Math.max(0, getSecondsFromHHMMSS(value));
        setEndTime(seconds);
        console.log("on blur seconds is " + seconds)
        console.log("on blur endTime is " + endTime)
        const time = toHHMMSS(seconds);
        
        setDisplayEndTime(time);
        console.log("on blur displaye time " +displayEndTime)
    };
    
    /*
    updates annotation text state on change
   */
    function handleChangeAnnotations(event){
        setAnnotations(event.target.value);
        console.log(annotations);
    }

    /*
    unhighlights start time when not clicked
    */
    function onBlurStartTime(event){
        const value = event.target.value;
        const seconds = Math.max(0, getSecondsFromHHMMSS(value));
        setStartTime(seconds);
        console.log("on blur seconds is " + seconds)
        console.log("on blur startTime " + startTime)
        const time = toHHMMSS(seconds);
        
        setDisplayStartTime(time);
        console.log("on blur displaye time " +displayStartTime)
    };
    
    /*
    updates start time state on change
   */
    function handleChangeStartTime(event){
            setDisplayStartTime(event.target.value);
            console.log("Onchange " + displayStartTime);
        };

    /*
    converts HH:MM:SS to secs format
    */
    const getSecondsFromHHMMSS = (value) => {
        const [str1, str2, str3] = value.split(":");
    
        const val1 = Number(str1);
        const val2 = Number(str2);
        const val3 = Number(str3);
    
        if (!isNaN(val1) && isNaN(val2) && isNaN(val3)) {
        // seconds
          return val1;
        }
    
        if (!isNaN(val1) && !isNaN(val2) && isNaN(val3)) {
        // minutes * 60 + seconds
          return val1 * 60 + val2;
        }
    
        if (!isNaN(val1) && !isNaN(val2) && !isNaN(val3)) {
        // hours * 60 * 60 + minutes * 60 + seconds
          return val1 * 60 * 60 + val2 * 60 + val3;
        }
    
        return 0;
      };

      /*
      converst sec to HH:MM:SS format
      */
      const toHHMMSS = (secs) => {
        const secNum = parseInt(secs.toString(), 10);
        const hours = Math.floor(secNum / 3600);
        const minutes = Math.floor(secNum / 60) % 60;
        const seconds = secNum % 60;
    
        return [hours, minutes, seconds]
          .map((val) => (val < 10 ? `0${val}` : val))
          .filter((val, index) => val !== "00" || index > 0)
          .join(":")
          .replace(/^0/, "");
    };

    /*
    submits object with annotation information to server to save it for specific upload 
    */
    function handleSubmit (event){
        event.preventDefault()
        if(endTime- startTime < 0){
            notifyBadTime();
        }
        else{
            axios.post(URL,{
                upload: props.id,
                start_time: Number(startTime),
                end_time: Number(endTime),
                annotation: annotations
            }).then(res =>{
                console.log("annotation worked");
                console.log(res);
                notifyFileUploaded();
            })
            .catch((err) => console.log(err));
        }
    }

/*
HTML for modal 
*/
    return (
        <div>
            <Card>
                <Modal>
                <form  className={classes.form} onSubmit={handleSubmit}>
                    <div className={classes.control}>
                        <label>
                            StartTime:
                            <input name="startTime" type="text" value={displayStartTime} onChange={handleChangeStartTime} onBlur={onBlurStartTime} required/>
                        </label>
                    </div>
                    
                    
                    <div className={classes.control}>
                        <label>
                        EndTime:
                        <input name="endTime" type="text" value={displayEndTime} onChange={handleChangeEndTime} onBlur={onBlurEndTime} required/>
                    </label>
                    </div>

                    <div className={classes.control}>
                        <label>
                            Annotations:
                        </label>
                            <p> Please type any annotations you wish to make into the box below</p>
                            <textarea rows = "15" cols = "150" onChange ={handleChangeAnnotations} value={annotations} required>
                
                            </textarea>
                        
                    </div>

                    <div className={classes.actions}>
                        <button>Submit</button>
                    </div>

                    

                </form>
                </Modal>
            </Card>
            <ToastContainer/>
        </div>
    )
}

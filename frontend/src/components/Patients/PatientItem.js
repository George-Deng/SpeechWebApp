import React from 'react';
import Card from '../ui/Card';
import classes from './PatientsItem.module.css';
import {Link} from 'react-router-dom';

/*
creates the patient item based on the information given back from the server to be displayed
has button to bring it to upload history page
*/

export default function PatientItem(props) {
    return (
        <li className={classes.item}>
            <Card>
                <div className={classes.content}>
                    Patient Name: {props.name}
                </div>
                <div className={classes.content}>
                <Link to = '/UploadHistory' params={{ id: props.id}}> 
                    <button>View Patient Uploads</button> 
                </Link> {/*figure out how to pass patient id prop*/}
                </div>
            </Card>
        </li>
    )
}

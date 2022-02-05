import React from 'react';
import PatientItem from './PatientItem';
import classes from "./PatientsItemsList.module.css"

/*
maps all of the recieved data to patient components so they can be displayed
*/
export default function PatientsItemList(props) {
    return (
        <ul className={classes.list}>
            {props.patientsList.map(patient => <PatientItem
                id = {patient.id}
                name = {patient.name}
                key = {patient.id}
            />)}
        </ul>
    )
}
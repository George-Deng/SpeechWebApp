import React from 'react'
import { useState, useEffect } from 'react';
import axios from 'axios';
import PatientsItemList from '../components/Patients/PatientItemsList';
/*
shows all patients under the selected doctor
*/

export default function PatientList() {
    const [isLoading, setIsloading] = useState(false);
    const [loadedPatients,setPatients] = useState([]);
  /*
  grabs all patients from server to be displayed on page
  */
  useEffect(()=>{
    setIsloading(true);
    axios.get('https://buddyguy-api.aswang.co/api/doctor/1/' // figure out how to concat doctor id at the end
      ).then(response =>{
        const patients =[];
        for(const key in response.data){
          const patient={
            id: key,
            ...response.data[key]
          };
          patients.push(patient);
        }
        console.log(response);
        console.log("THIS IS PATIENTS LIST")
        setIsloading(false);
        setPatients(patients);
    });
  },[]);

  
/*
shows loading while grabbing patients from server
*/
  if(isLoading){
    return (
      <section>
        <p>
          Loading...
        </p>
      </section>
    );
  }

/*
HTML for Patient List
*/
    return (
        <div>
            <PatientsItemList patientsList={loadedPatients}/>
        </div>
    )
}
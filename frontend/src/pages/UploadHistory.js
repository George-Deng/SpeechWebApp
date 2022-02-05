import React from 'react'
import UploadList from '../components/Uploads/UploadList'
import { useState, useEffect } from 'react';
import axios from 'axios';

/*
shows all upload history under the selected patient
*/

export default function UploadHistory(props) {
    const [isLoading, setIsloading] = useState(false);
    const [loadedUploads,setUploads] = useState([]);
    
   /*
  grabs all patients uploads from server to be displayed on page
  */
  useEffect(()=>{
    setIsloading(true);
    axios.get('https://buddyguy-api.aswang.co/api/upload/'
    ).then(response =>{
        const uploads =[];
        for(const key in response.data){
          const upload={
            id: key,
            ...response.data[key]
          };
          if(upload.patient === null){ // create parameter for patient id
            uploads.push(upload);
          }
        }
        console.log(response);
        setIsloading(false);
        setUploads(uploads);
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
HTML for Upload History 
*/
    return (
        <div>
            <UploadList uploads={loadedUploads}/>
        </div>
    )
}



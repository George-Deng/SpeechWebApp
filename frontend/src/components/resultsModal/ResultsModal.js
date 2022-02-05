import React from 'react'
import { useState, useEffect} from 'react';
import axios from 'axios';
import classes from './ResultsModal.module.css';
import Card from '../ui/Card';
import Modal from '../Modal/Modal';

/*
request prediction results from server to display on results modal
*/
export default function ResultsModal(props) {
    const [isLoading, setIsloading] = useState(false);
    const [loadedResults,setResults] = useState([]);
    const [loadedParkinsonsResults,setResultsParkinsons] = useState([]);
    let URL ='https://buddyguy-api.aswang.co/api/gender/' + props.id;
    let URL1 ='https://buddyguy-api.aswang.co/api/parkinsons/' + props.id;
    console.log(URL);
    console.log(URL1);
    
  /*
  grabs all predictions  from server to be displayed on page
  */
  useEffect(()=>{
    setIsloading(true);
    const responseOne = axios.get( URL);
    const responseTwo = axios.get(URL1);
    //use /access the results

    axios.all([responseOne,responseTwo]).then(axios.spread((...responses)=>{
      setResults(responses[0]);
      setResultsParkinsons(responses[1])
      setIsloading(false);
    })).catch(errors=>{
      console.log(errors);
    });
  },[URL,URL1]);

/*
shows loading while from server
*/
  if(loadedResults.length === 0 || isLoading){
    return (
      <section className='modal'>
        <p>
          Loading...
        </p>
      </section>
    );
  }

/*
HTML for modal 
*/
  if(loadedResults.length !== 0){
    return (
            <Card className={classes.item}>
                <Modal>
                    {/* sometimes loaded results is empty, axios didnt actulaly go up 
                    Sometimes axios is working and then sometimes it doesn't* request is made multiple times for some reason*/}
                    <div>Gender Predicion Test Results: {loadedResults.data.prediction}</div>
                    <div>Parkinsons Predicion Test Results: {loadedParkinsonsResults.data.prediction}</div>
                    
                    
                    
                
              </Modal>
            </Card>
          
        
      
        );
    }
  
}



   
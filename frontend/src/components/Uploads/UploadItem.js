import React from 'react';
import Card from '../ui/Card';
import {useState} from 'react';
import classes from './UploadItem.module.css';
import Backdrop from '../Modal/Backdrop';
import ResultsModal from '../resultsModal/ResultsModal';
import AnnotateModal from '../annotateModal/AnnotateModal';
/*
creates the upload item based on the information given back from the server to be displayed
has button to trigger results modal and annotation modal to be displayed
*/

export default function UploadItem(props) {
    let url_path = "" + props.file;
    const[modalResultsIsOpen, setModalResultsIsOpen] = useState(false);
    const[modalAnnotateIsOpen, setModalIsOpen] = useState(false);

    function resultHandler(){
         setModalResultsIsOpen(true);
       
    }

    function annotateResultHandler(){
        setModalIsOpen(true);
    }

    function closeModalHandler(){
        setModalIsOpen(false);
        setModalResultsIsOpen(false);
    }

   

    return (
        <li className={classes.item}>
            <Card>
                <div className={classes.content}>
                    {props.uploaded_at}
                </div>
                <div className={classes.content}>
                    <a href={url_path}>{url_path}</a>
                </div>
             
                    <div className={classes.content}>
                        <button onClick={resultHandler}>View Results</button> 
                        <button onClick={annotateResultHandler}>Annotate</button> 
                    </div>
                
            { modalResultsIsOpen && <ResultsModal id ={props.id}/>}
            { modalAnnotateIsOpen && <AnnotateModal id ={props.id}/>}
            { (modalResultsIsOpen || modalAnnotateIsOpen ) && <Backdrop onClick={closeModalHandler}/>}
            </Card>
            
        </li>
    )
}

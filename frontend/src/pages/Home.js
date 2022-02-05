import React from 'react'
import { useState} from 'react';
import axios from 'axios';
import AudioReactRecorder, { RecordState } from 'audio-react-recorder'
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

 /*
    Home page allows for audio recording, uploads, and downloads 
    of wav files as well as includes a text area for the user
    to type in a script to read.
 */
 
export default function HomePage() {
    const [selectedFile,setFile] = useState(null);
    const [selectedRecording,setRecordingBlob] = useState(null);
    const [isRecording, setRecording] = useState(null);
    const [audioData, setAudioData] = useState(null);
    const URL = 'https://buddyguy-api.aswang.co/api/upload/';
    const confij = {headers:{'Access-Control-Allow-Headers': 'Content-Disposition'}}
    const notify = () =>toast("You haven't recorded anything yet!");
    const notifyFileNotSelected =  () =>toast("You haven't chosen a file!");
    const notifyFileUploaded =  () =>toast("File was successfuly uploaded!");
   
   
    function start(){
        setRecording(RecordState.START);
    }

    function pause(){
        setRecording(RecordState.PAUSE);
    }

    function stop(){
        setRecording(RecordState.STOP);
    }

    /*
    When stop button is called recording is stopped
    and audio file is saved. Audio file is then able 
    to be uploaded or played again
    */
    function onStop(data){
        setAudioData(data);
        setRecordingBlob(data.blob);
        console.log('onStop: audioData', data);
    }

    /*
    prepares files to be uploaded
    */
    function uploadRecording(){
        if(selectedRecording == null){
            notify();
        }else{
            blobuploadHandler(selectedRecording.blob);
            // tell user file is uploaded
        }
    }

    /*
    allows files to be downloaded as a wav file
    */
    function downLoadRecording(){
        if(selectedRecording == null){
            notify();
        } else{

        const fileDownloadUrl = window.URL.createObjectURL(selectedRecording);
        const link = document.createElement('a');
        link.href = fileDownloadUrl;
        link.setAttribute('download', 'RecordedAudio.wav');
        link.click();
        }

    }
    
    /*
    prepares files to be uploaded
    */
    function fileSelectedHandler (event){
        setFile(event.target.files[0]);
        console.log(event.target.files[0]);
    }

    
    /*
    sends uploaded file to server
    */
    function fileuploadHandler (){
        if(selectedFile == null){
            notifyFileNotSelected();
        }
        else{
            const fd = new FormData();
            fd.append('file',selectedFile ,selectedFile.name);
            console.log(fd);
            axios.post(URL, fd, confij)
            .then(res =>{
                console.log(res);
                notifyFileUploaded();
            })
            .catch((err) => 
            console.log(err));
        }
    }

    /*
    sends recorded file to server
    */
    function blobuploadHandler (){
        const fd = new FormData();
        fd.append('file',selectedRecording);
        axios.post(URL, fd, confij)
        .then(res =>{
            console.log(res);
            notifyFileUploaded();
        })
        .catch((err) => console.log(err));
    }

    /*
    this is all the HTML for the Home Page
    */
    return (
        <div>
            <div>
                <input type="file" accept='.mp3,.wav' onChange={fileSelectedHandler}/>
                <button onClick={fileuploadHandler}>Upload</button>
            </div>

            <div>
            <audio
                id='audio'
                controls
                src={audioData ? audioData.url : null}
        ></audio>
                <h3>Instructions:</h3>
                <p>Make sure to speak clearly and directly into your microphone</p>
                <AudioReactRecorder state={isRecording} onStop={onStop} backgroundColor='rgb(25,115,245)'/>
                
                    
                
                <button onClick={start}>Start</button>
                
                <button onClick={pause}>Pause</button>
                
                <button onClick={stop}>Stop</button>
                
                <button onClick={uploadRecording}>Upload Recording</button>
                
                <button onClick={downLoadRecording}>Download Recorded File</button>
                
               
            </div>

            <div className="speechRegiment">
                <h3>Notes:</h3>
                <p>You can type in a pre planned scenario in the text area below for you to read off while recording</p>
            <textarea rows = "15" cols = "150">
        
            </textarea>
            </div>

           <ToastContainer/>
        </div>
        

        
    );
}

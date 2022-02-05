import React from 'react';
import classes from './UploadList.module.css';
import UploadItem from './UploadItem';

/*
maps all of the recieved data to upload components so they can be displayed
*/
export default function UploadList(props) {
    return (
        <ul className={classes.list}>
            {props.uploads.map(uploads => <UploadItem 
                uploaded_at = {uploads.uploaded_at}
                file= {uploads.file}
                key = {uploads.id}
                id = {uploads.id}
            />)}
        </ul>
    )
}

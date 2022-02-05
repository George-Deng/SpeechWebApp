import React from 'react'

/*
gives modal appearance
*/
export default function Modal(props) {
    return (
      <div className='modal'>
        {props.children}    
      </div>
      
    );
}

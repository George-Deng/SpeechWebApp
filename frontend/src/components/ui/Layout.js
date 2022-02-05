import React from 'react'
import classes from './Layout.module.css'

/*
makes sures card doesn't span the entire page
*/
export default function Layout(props) {
    return (
        <div>
            <main className ={classes.main}> {props.children} </main>
        </div>
    )
}

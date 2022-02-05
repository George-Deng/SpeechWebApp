import React from 'react'
import {Link} from 'react-router-dom'
import classes from './MainNavigation.module.css'
import axiosInstance from '../../axiosApi'
import { useHistory } from 'react-router'

export default function MainNavigation(props) {
    const history = useHistory();

    function handleLogout() {
        try {
            const response = axiosInstance.post('https://buddyguy-api.aswang.co/api/token/blacklist/', {
                "refresh_token": localStorage.getItem("refresh_token")
            }).then(response=>{
                localStorage.removeItem('access_token');
                localStorage.removeItem('refresh_token');
                axiosInstance.defaults.headers['Authorization'] = null;
                history.push('/');
                return response;
            })
            
        }
        catch (error) {
            console.log(error);
        }
    }


    return (
        <header className={classes.header}>
            <div className= {classes.logo}>
                {props.title}
            </div>
            <nav>
                <ul>

                    <li>
                        <Link to='/home'>Home Page</Link>
                    </li>

                    <li>
                        <Link to='/UploadHistory'>Upload History</Link>
                    </li>

                    <li>
                        <Link to='/patientList'>Patient List </Link>
                    </li>
                    <li>
                    <div className={classes.actions}>
                        <button onClick={handleLogout}>Logout</button>
                    </div>
                    </li>
                </ul>
            </nav>
        </header>
    )
}

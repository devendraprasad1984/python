import React, {useRef} from 'react';
import {POST} from "../common/post";
import '../App.css';

export default function Login(props) {
    const usernameRef = useRef();
    const passwordRef = useRef();

    const handleLogin = event => {
        const username = usernameRef.current.value;
        const password = passwordRef.current.value;
        const body = {username, password};
        POST('/auth/', body, res => props.setToken(res.token));
    }
    const handleRegister = event => {
        const username = usernameRef.current.value;
        const password = passwordRef.current.value;
        const body = {username, password};
        POST('/api/users/', body, res => console.log(res));
    }

    return <div className="column login">
        <h1>Login Page</h1>
        <input ref={usernameRef} type='text' placeholder='usernanme'/>
        <input ref={passwordRef} type='password' placeholder='password'/>
        <div className='row'>
            <button onClick={handleLogin}>Login</button>
            <button onClick={handleRegister}>Register</button>
        </div>
    </div>;
}

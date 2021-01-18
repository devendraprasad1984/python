import React, {useRef, useState} from 'react';
import {POST} from "../common/post";
import '../App.css';

export default function Login(props) {
    const [msg, setMsg] = useState('');
    const usernameRef = useRef();
    const passwordRef = useRef();

    const handleLogin = event => {
        const username = usernameRef.current.value;
        const password = passwordRef.current.value;
        const body = {username, password};
        POST('/auth/', body, res => {
            setMsg(typeof res.token === 'string' ? 'login successfully' : 'failed login');
            props.setToken(res.token);
        });
    }
    const handleRegister = event => {
        const username = usernameRef.current.value;
        const password = passwordRef.current.value;
        const body = {username, password};
        POST('/api/users/', body, res => {
            const checkResponse = res.username;
            setMsg(typeof checkResponse !== 'string' ? checkResponse[0] : 'registered successfully')
        });
    }

    return <div className="column login">
        <h1>Login Page</h1>
        <input ref={usernameRef} type='text' placeholder='usernanme'/>
        <input ref={passwordRef} type='password' placeholder='password'/>
        <div className='row'>
            <button onClick={handleLogin}>Login</button>
            <button onClick={handleRegister}>Register</button>
        </div>
        <div>{msg}</div>
    </div>;
}

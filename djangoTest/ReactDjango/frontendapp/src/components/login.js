import React, {useRef} from 'react';

export default function Login(props) {
    // const [cred, setCred]=useState({username:'',password:''});
    const usernameRef = useRef();
    const passwordRef = useRef();

    const handleLogin = event => {
        const username = usernameRef.current.value;
        const password = passwordRef.current.value;
        const payload = {
            method: 'POST'
            , headers: {'Content-Type': 'application/json'}
            , body: JSON.stringify({username, password})
        }
        fetch('http://127.0.0.1:8000/auth/', payload)
            .then(res=>res.json())
            .then(res => console.log(res))
            .catch(err => console.error(err))
    }

    return <div className="App">
        <h1>Login Page</h1>
        <input ref={usernameRef} type='text' placeholder='usernanme'/>
        <input ref={passwordRef} type='password' placeholder='password'/>
        <button onClick={handleLogin}>Login</button>
    </div>;
}

import React from 'react';
import './App.css';
import Login from "./components/login";
import Books from "./components/books";

function App() {
    const [global, setGlobal] = React.useState({token: ''});
    const setToken = tok => {
        setGlobal({token: tok});
    }
    const checkUserAuth = () => {
        return global.token != '' ? <h1>User Authenticated...</h1> : null
    }
    return (
        <div className="App">
            {checkUserAuth()}
            <Login setToken={setToken}/>
            <Books {...global}/>
        </div>
    );
}

export default App;

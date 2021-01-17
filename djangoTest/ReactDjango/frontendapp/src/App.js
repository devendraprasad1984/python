import React from 'react';
import './App.css';
import Login from "./components/login";
import Books from "./components/books";

function App() {
    const [global, setGlobal] = React.useState({token: ''});
    const setToken = tok => {
        setGlobal({token: tok});
    }
    return (
        <div className="App">
            <Login setToken={setToken}/>
            <Books {...global}/>
        </div>
    );
}

export default App;

import React from 'react';
import './App.css';
import Login from "./components/login";
import Books from "./components/books";
import Todo from "./components/todo";
import NewToDo from "./components/newTodo";

function App() {
    const [global, setGlobal] = React.useState({token: ''});
    const setToken = tok => {
        setGlobal({token: tok});
    }
    return (
        <div className="App">
            <h1><a href='http://localhost:8000/home'>django website</a></h1>
            <Login setToken={setToken}/>
            <Books {...global}/>
            <Todo {...global}/>
            <NewToDo {...global}/>
        </div>
    );
}

export default App;

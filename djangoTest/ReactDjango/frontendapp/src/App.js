import './App.css';
import Login from "./components/login";

function App() {
    const setToken=token=>{
        console.log(token);
    }
    return (
        <div className="App">
            <h1>Login Page django Practices</h1>
            <Login setToken={setToken}/>
        </div>
    );
}

export default App;

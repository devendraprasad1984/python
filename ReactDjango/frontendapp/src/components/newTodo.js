import React, {useState, createRef} from 'react';
import {GET} from "../common/get";
import '../App.css'

export default function NewToDo(props) {
    const {token} = props;
    const todoRef=createRef()
    const [todo, setTodo] = useState([]);
    const [load, setLoad] = useState(false);
    const loader = <i className="fa fa-refresh fa-spin"></i>;

    const fetchToDo = () => {
        setLoad(true);
        GET('/todos/list/', {token}, res => {
            // console.log('todo',res)
            setTodo(res)
            setTimeout(() => setLoad(false), 1000);
        })
    }
    const handleToDoDelete=(id)=>{
        console.log('todo to delete',id)
        GET('/todos/delete_todo/'+id,{token},res=>{
            fetchToDo()
        })
    }
    const displayToDo = () => {
        if (todo.length === 0 || todo === undefined) return null
        return todo.map((x, i) => <div key={'todo' + i} className={'row'} style={{padding:1}}>
            <span>{x.fields.content}</span>
            <button onClick={()=>handleToDoDelete(x.pk)}>delete</button>
        </div>);
    }
    const addToDo=()=>{
        let todoName=todoRef.current.value
        GET('/todos/add_todo/'+todoName,{token},res=>{
            todoRef.current.value=''
            todoRef.current.focus()
            fetchToDo()
        })
    }
    return <div>
        <h2>ToDo Listing using different todo app</h2>
        <div className={'row'}>
            <input ref={todoRef} type={'text'} style={{width:'80%'}}/>
            <button onClick={addToDo}>Add</button>
            <button onClick={fetchToDo}>Refresh</button>
        </div>
        {displayToDo()}
    </div>
}

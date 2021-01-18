import React, {useState} from 'react';
import {GET} from "../common/get";
import '../App.css'

export default function Todo(props) {
    const {token} = props;
    const [tasks, setTasks] = useState([]);
    const [load, setLoad] = useState(false);
    const loader = <i className="fa fa-refresh fa-spin"></i>;

    const fetchBooks = event => {
        setLoad(true);
        GET('/api/task-list/', {token}, res => {
            if (res.detail === undefined)
                setTasks(res);
            else
                setTasks([{title: res.detail}])
            setTimeout(() => setLoad(false), 1000);
        })
    }
    const displayBooks = () => {
        return tasks.map((x, i) => <div key={'task' + i} className={'row'}>
            <span>{x.title}</span>
            <span><i className={`fa ${x.completed?'fa-check':'fa-times'}`}></i></span>
        </div>);
    }

    return <div>
        <h2>Tasks</h2>
        <button onClick={fetchBooks}>{load ? loader : null} Task</button>
        {displayBooks()}
    </div>
}

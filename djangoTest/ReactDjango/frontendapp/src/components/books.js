import React, {useState} from 'react';
import {GET} from "../common/get";

export default function Books(props) {
    const {token} = props;
    const [books, setBooks] = useState([]);
    const [load, setLoad] = useState(false);
    const loader=<i className="fa fa-refresh fa-spin"></i>;

    const fetchBooks = event => {
        setLoad(true);
        GET('/api/books/', res => {
            setBooks(res);
            setTimeout(()=>setLoad(false),1000);
        })
    }
    const displayBooks = () => {
        return books.map((x, i) => <div key={'bk' + i}>
            <span>{x.title}</span>
        </div>);
    }

    return <div>
        <h2>Books listed</h2>
        <span className="fa fa-facebook"></span>
        <span className="fa fa-twitter"></span>
        <p>{token}</p>
        <button onClick={fetchBooks}>{load ? loader: null} Load Books</button>
        {displayBooks()}
    </div>
}

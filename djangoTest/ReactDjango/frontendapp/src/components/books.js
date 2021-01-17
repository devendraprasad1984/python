import React, {useState} from 'react';
import {GET} from "../common/get";

export default function Books(props) {
    const {token} = props;
    const [books, setBooks] = useState([]);

    const fetchBooks = event => {
        GET('/api/books/', res => setBooks(res))
    }
    const displayBooks = () => {
        return books.map((x, i) => <div key={'bk' + i}>
            <span>{x.title}</span>
        </div>);
    }

    return <div>
        <h2>Books listed</h2>
        <p>{token}</p>
        <button onClick={fetchBooks} className='color1'>Load Books</button>
        {displayBooks()}
    </div>
}

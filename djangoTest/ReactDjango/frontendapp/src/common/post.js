export function POST(url, body, callback){
    const URI='http://127.0.0.1:8000'+url;
    const payload = {
        method: 'POST'
        , headers: {'Content-Type': 'application/json'}
        , body: JSON.stringify(body)
    }
    fetch(URI, payload)
        .then(res=>res.json())
        .then(res => callback(res))
        .catch(err => callback(err))
}

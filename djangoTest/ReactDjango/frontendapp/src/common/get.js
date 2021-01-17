export function GET(url, callback){
    const URI='http://127.0.0.1:8000'+url;
    const payload = {
        method: 'GET'
    }
    fetch(URI, payload)
        .then(res=>res.json())
        .then(res => callback(res))
        .catch(err => callback(err))
}

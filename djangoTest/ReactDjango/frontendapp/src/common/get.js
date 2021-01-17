export function GET(url,params, callback){
    const URI='http://127.0.0.1:8000'+url;
    const payload = {
        method: 'GET',
        headers:{
            'Content-Type':'application/json',
            Authorization: `Token ${params.token}`
        }
    }
    fetch(URI, payload)
        .then(res=>res.json())
        .then(res => callback(res))
        .catch(err => callback(err))
}

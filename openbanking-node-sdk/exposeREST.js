const express=require('express');
const {getAccounts,getTransactions} = require('./api');
const ConfigError = require('./config-error');

let authToken=undefined;

const books = [
    {title: 'Harry Potter', id: 1},
    {title: 'Twilight', id: 2},
    {title: 'Lorien Legacies', id: 3}
]

const app=express();
app.use(express.json());

app.get('/', (req,res)=> {
    res.send('welcome to node api for hackathon open banking 2020 - RBS');
});

app.get('/api/books', (req,res)=> {
    res.send(books);
});

app.get('/api/accounts', async (req,res)=> {
    try{
        console.log('auth token from ob api',authToken);
        const accounts = await getAccounts(authToken);
        console.log('accounts are', accounts);
        res.json(accounts);
    }catch (error) {
        if (error instanceof ConfigError)
            console.log('Configuration error: ', error.message);
        else
            throw error;
    }
});

app.get('/api/transactions/:accountId', (req,res)=> {
    res.send(books);
});

const startServer=function(authorisedAccessToken){
    authToken=authorisedAccessToken;
    const port = process.env.PORT || 6200;
    app.listen(port, () => console.log(`Listening on port ${port}..`));

}

module.exports={
    startServer
}
const accountsUri = './accountsEndpoints/listOfAccounts.json'
const transactionUri = './accountsEndpoints/listOfTransactions.json'
const accountsList = document.getElementById('accountsList');
let trasactionData = undefined;
const contentHeader = document.getElementById('contentHeader');
const contentData = document.getElementById('contentData');
let synthesis ='speechSynthesis' in window ? window.speechSynthesis:undefined;
const symbols = {
    inr: '₹'
    , pound: '£'
}

function initAccountApiCall() {
    console.log('accounts are being fatched');
    fetch(accountsUri).then(res => res.json()).then(data => {
        let rows = data['Data']['Account'];
        let elements = [];
        for (let i in rows) {
            let row = rows[i];
            let accId = row.AccountId;
            let title = [row.AccountSubType, row.AccountType, row.Currency, row.Description, row.Nickname].join(' - ');
            // console.log(accId, title);
            let strElem = '<a href="#" title="' + title + '" onclick="handleAccountClick(this)">' + accId + '</a>';
            elements.push(strElem);
            accountsList.innerHTML = elements.join('');
        }
    });
}

function initTransactionApiCall() {
    //toastr.info('plz wait...');
    console.log('transactions are being monitored');
    fetch(transactionUri).then(res => res.json()).then(data => {
        trasactionData = data;
        // console.log('Transactions have been fetched');
    });
}

document.addEventListener("DOMContentLoaded", function () {
    initAccountApiCall();
    initTransactionApiCall();
});

function handleLinkActivate(curLink){
    let links=Array.from(accountsList.childNodes);
    links.map(x=>x.classList.remove('active'));
    curLink.classList.add('active');
}

function handleAccountClick(that) {
    let accId = that.innerHTML;
    let title = that.getAttribute('title');
    handleLinkActivate(that);

    let arr = [];
    arr.push('<div class="accountHeadLine"><span class="orange">Story</span> for ' + accId + ' as follows</div>');
    arr.push('<div>' + title + '</div>');
    contentHeader.innerHTML = arr.join('');
    let allDebits = [];
    let allCredits = [];
    // console.log(accId,title,trasactionData);
    let allData = trasactionData['Data']['Transaction'];
    for (let i in allData) {
        let row = allData[i];
        if (row.AccountId !== accId) continue;
        // console.log(row);
        let indicator = row.CreditDebitIndicator;
        if (indicator === 'Credit') {
            allCredits.push(parseFloat(row.Amount.Amount));
        } else if (indicator === 'Debit') {
            allDebits.push(parseFloat(row.Amount.Amount));
        }
    }
    // console.log('Debits', allDebits,'Credits', allCredits);

    let mainStr = [];
    let maxCredit = Math.max(...allCredits);
    let minCredit = Math.min(...allCredits);
    let maxDebit = Math.max(...allDebits);
    let minDebit = Math.min(...allDebits);
    // mainStr.push('<div>Highest Credit: ' + maxCredit + ' Lowest Credit: ' + minCredit + '</div>');
    // mainStr.push('<div>Highest Debit:' + maxDebit + ' Lowest Debit: ' + minDebit + '</div>');
    mainStr.push('<div>For Month July 2020, You have largest Credit of <span class="green">' + symbols.inr + '/' + symbols.pound + maxCredit + '</span> and largest withdrawl of<span class="red"> ' + symbols.inr + '/' + symbols.pound + maxDebit + '</span></div>');
    let arrContents = [];
    arrContents.push('<div style="margin-top:1rem;"></div>');
    arrContents.push(mainStr.join(''));
    contentData.innerHTML = arrContents.join('');
}

function speakOut() {
    //https://www.digitalocean.com/community/tutorials/how-to-build-a-text-to-speech-app-with-web-speech-api
    //Note: There is a limit to the size of text that can be spoken in an utterance. The maximum length of the text that can be spoken in each utterance is 32,767 characters.
    // if ('speechSynthesis' in window) {
    if(typeof synthesis==="undefined"){
        console.log('no voice assistant present');
        return;
    }
    let voice = synthesis.getVoices().filter(function (voice) {
        // return voice.lang=== 'en-US';
        return voice.lang=== 'hi-IN';
    })[0];
    let utterance = new SpeechSynthesisUtterance(contentData.innerText);
    utterance.lang='en-US';
    utterance.voice=voice;
    utterance.pitch = 1;
    utterance.rate = 1;
    utterance.volume = 0.9;
    // console.log(synthesis,utterance,voice);
    synthesis.speak(utterance);

    // var utterance = new SpeechSynthesisUtterance("Hello World");
    // utterance.text = "My name is Glad.";
    // synthesis.speak(utterance);


}

function stopPlay() {
    if(typeof synthesis==="undefined"){
        console.log('no voice assistant present');
        return;
    }
    synthesis.paused=true;
    synthesis.speaking=false;
    console.log('stopping...',synthesis);
}
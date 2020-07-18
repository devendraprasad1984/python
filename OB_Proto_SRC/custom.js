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
    mainStr.push('<p>Your Account Summary for Month July 2020, You have received largest sum of <span class="bggreen">' + symbols.inr + maxCredit + '</span> and biggest paid out was <span class="bgred"> ' + symbols.inr + maxDebit + '</span></p>');
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
        return voice.lang=== 'en-US';
    })[0];
    let utterance = new SpeechSynthesisUtterance(contentData.innerText);
    utterance.lang='en-US';
    utterance.voice=voice;
    utterance.pitch = 1;
    utterance.rate = 0.9;
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


function googleTranslateElementInit() {
    new google.translate.TranslateElement({
        pageLanguage: 'en',
        includedLanguages: 'hi',
        autoDisplay: false
    }, 'google_translate_element');
    var a = document.querySelector("#google_translate_element select");
    a.selectedIndex = 1;
    a.dispatchEvent(new Event('change'));
}


function changeLanguage(langs){
    let src=langs.split('-')[0];
    let tgt=langs.split('-')[1];
    let urlg = 'https://translation.googleapis.com/language/translate/v2?key=API_Key&source='+src+'&target='+tgt+'&q=' + contentData.innerText;
    let urly='https://translate.yandex.com/?lang='+langs.toLowerCase()+'&text='+contentData.innerText
    fetch(urly).then(res=>console.log(res, res.body));
}

function generateSampleNarrative(){
    let mainStr=[]
    mainStr.push('Loans in your account ending 8787 & 9898 has decreased by 10% since you taken it in 2018 due to interest rate being changed by 1%. You have a total deposit of 5000000 and you regularly receive 500000 as part of your salary. Your majors spends are in clothing ie 30000 and leisure ie 200000 but you have saved enough in all your savings. We have some savings offers for you, would you want to proceed?');
    let arrContents = [];
    arrContents.push('<div style="margin-top:1rem;"></div>');
    arrContents.push(mainStr.join(''));
    contentData.innerHTML = arrContents.join('');
}
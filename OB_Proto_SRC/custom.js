const accountsUri = './accountsEndpoints/listOfAccounts.json';
const transactionUriPage0 = './accountsEndpoints/transPage0.json';
const transactionUriPage1 = './accountsEndpoints/transPage1.json';
const transactionUriPage2 = './accountsEndpoints/transPage2.json';
const transactionUriPage3 = './accountsEndpoints/transPage3.json';
const accountsList = document.getElementById('accountsList');
const contentHeader = document.getElementById('contentHeader');
const contentData = document.getElementById('contentData');
const contentLength = document.getElementById('contentLength');
const idActions = document.getElementById('idActions');

let trasactionData = [];
let synthesis = 'speechSynthesis' in window ? window.speechSynthesis : undefined;
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
            let accId = row.Account[0].Identification;
            let accIdForTrans = row.AccountId;
            let title = [row.Nickname, row.Currency, row.Account[0].SchemeName].join(' / ');
            // console.log(accId, title);
            let strElem = '<a href="#" title="' + title + '" onclick="handleAccountClick(this)" accid="' + accIdForTrans + '">' + accId + '</a>';
            elements.push(strElem);
            accountsList.innerHTML = elements.join('');
        }
    });
}

function initTransactionApiCall() {
    //toastr.info('plz wait...');
    console.log('transactions are being monitored');
    for (let uri of [transactionUriPage0, transactionUriPage1, transactionUriPage2, transactionUriPage3]) {
        fetch(uri).then(res => res.json()).then(data => {
            trasactionData.push(data['Data']['Transaction']);
            // console.log(trasactionData);
        });
    }
}

function getContentLength() {
    setInterval(function () {
        contentLength.innerHTML = '<span>' + contentData.innerText.length + ' Characters</span>';
    }, 500)
}

document.addEventListener("DOMContentLoaded", function () {
    initAccountApiCall();
    initTransactionApiCall();
    getContentLength();
});

function handleLinkActivate(curLink) {
    let links = Array.from(accountsList.childNodes);
    links.map(x => x.classList.remove('active'));
    curLink.classList.add('active');
}

function handleAccountClick(that) {
    let accTransId = that.getAttribute('accid');
    let accId = that.innerHTML;
    let title = that.getAttribute('title');
    handleLinkActivate(that);

    let arr = [];
    arr.push('<div class="accountHeadLine"><span class="orange">Story</span> for <span class="red">' + accId + '</span> as follows</div>');
    arr.push('<div>' + title + '</div>');
    contentHeader.innerHTML = arr.join('');
    let allDebits = [];
    let allCredits = [];
    // console.log(accId,title,trasactionData);
//    let allData = trasactionData['Data']['Transaction'];
    for (let trans of trasactionData) {
        console.log('working through', trans);
        for (let j in trans) {
            let row = trans[j];
            if (row.AccountId !== accTransId) continue;
            // console.log(row);
            let indicator = row.CreditDebitIndicator;
            if (indicator === 'Credit') {
                allCredits.push(parseFloat(row.Amount.Amount));
            } else if (indicator === 'Debit') {
                allDebits.push(parseFloat(row.Amount.Amount));
            }
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
    mainStr.push('<div>Welcome Mr Prasad,</div>');
    mainStr.push('<div>Your Account Summary for Month July 2020, You have received largest sum of <span class="bggreen">' + symbols.inr + maxCredit + '</span> and biggest paid out was <span class="bgred"> ' + symbols.inr + maxDebit + '</span></div>');
    let arrContents = [];
    arrContents.push('<div style="margin-top:1rem;"></div>');
    arrContents.push(mainStr.join(''));
    contentData.innerHTML = arrContents.join('');
}

function speakOut() {
    //https://www.digitalocean.com/community/tutorials/how-to-build-a-text-to-speech-app-with-web-speech-api
    //Note: There is a limit to the size of text that can be spoken in an utterance. The maximum length of the text that can be spoken in each utterance is 32,767 characters.
    // if ('speechSynthesis' in window) {
    if (typeof synthesis === "undefined") {
        console.log('no voice assistant present');
        return;
    }
    let voice = synthesis.getVoices().filter(function (voice) {
        // return voice.lang=== 'en-US';
        return voice.lang === 'en-US';
    })[0];
    let utterance = new SpeechSynthesisUtterance(contentData.innerText);
    utterance.lang = 'en-US';
    utterance.voice = voice;
    utterance.pitch = 1;
    utterance.rate = 0.9;
    utterance.volume = 0.9;
    // console.log(synthesis,utterance,voice);
    // synthesis.speak(utterance);
    speechUtteranceChunker(utterance, {
        chunkLength: 120
    }, function () {
    });
    // var utterance = new SpeechSynthesisUtterance("Hello World");
    // utterance.text = "My name is Glad.";
    // synthesis.speak(utterance);
}

function stopPlay() {
    if (typeof synthesis === "undefined") {
        console.log('no voice assistant present');
        return;
    }
    synthesis.paused = true;
    synthesis.speaking = false;
    console.log('stopping...', synthesis);
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


function changeLanguage(langs) {
    let src = langs.split('-')[0];
    let tgt = langs.split('-')[1];
    let urlg = 'https://translation.googleapis.com/language/translate/v2?key=API_Key&source=' + src + '&target=' + tgt + '&q=' + contentData.innerText;
    let urly = 'https://translate.yandex.com/?lang=' + langs.toLowerCase() + '&text=' + contentData.innerText
    fetch(urly).then(res => console.log(res, res.body));
}

function handleActionActivate(curLink) {
    let links = Array.from(idActions.children);
    links.map(x => x.classList.remove('bgred'));
    curLink.classList.add('bgred');
}

function generateSummary(curElem) {
    handleActionActivate(curElem);
    let mainStr = []
    mainStr.push('<div>Welcome Mr Prasad,</div>');
    mainStr.push('<div>Loans in your account ending 8 7 8 7 and 9 8 9 8 has decreased by 10 percent since you taken it in 2018 due to interest rate being changed by 1 basis points. You have a total deposit of <span class="green">' + symbols.inr + '5000000</span> and you regularly receive <span class="green">' + symbols.inr + '500000</span> as part of your salary. Your majors spends are in clothing, for example, <span class="red">' + symbols.inr + '30000</span> and leisure, for example, <span class="red">' + symbols.inr + '200000</span> but  not too worry, we are with you to maintain funds. We have some savings offers for you, would you want to proceed?</div>');
    let arrContents = [];
    arrContents.push('<div style="margin-top:1rem;"></div>');
    arrContents.push(mainStr.join(''));
    contentData.innerHTML = arrContents.join('');
}

function generateMoratorium(curElem) {
    handleActionActivate(curElem);
    let mainStr = []
    mainStr.push('<div>You have moratorium activated on acount ending 8 7 8 7, Your next due is in 10 september 2020. There is not request being submitted on account ending 9 8 9 8, would you want to generate a request</div>');
    mainStr.push('<div>We have created one for you and sent consent link to your registered email</div>');
    let arrContents = [];
    arrContents.push('<div style="margin-top:1rem;"></div>');
    arrContents.push(mainStr.join(''));
    contentData.innerHTML = arrContents.join('');
}

function generateTop5(curElem) {
    handleActionActivate(curElem);
    let mainStr = []
    mainStr.push('<div>Welcome, Your total Debit and Credits are <span class="red">'+symbols.pound+'1600000</span> and <span class="green">'+symbols.pound+'2200000</span> respectively</div>');
    mainStr.push('<div>you need to redo KYC as soon as possible,</div>');
    mainStr.push('<div>you have recent debits of <span class="orange">100, 145, 10</span> pounds for insurance premium, upi to account ending 7 6 3 5 and lower monthly average balance,</div>');
    mainStr.push('<div>you have received your salary 2 days back. Enjoy Spending,</div>');
    mainStr.push('<div>interest rates on fixed deposits has been slashed down by 1 basis point,</div>');
    mainStr.push('<div>3 of your deposits are going to mature within 2 months. Congrats</div>');
    let arrContents = [];
    arrContents.push('<div style="margin-top:1rem;"></div>');
    arrContents.push(mainStr.join(''));
    contentData.innerHTML = arrContents.join('');
}

function generateOffers(curElem) {
    handleActionActivate(curElem);
    let mainStr = []
    mainStr.push('<div>avail a personal loan of upto 1000000 at rate of 9.75 per Annum reducing,</div>');
    mainStr.push('<div>we can drop cash to your registered home, just say alexa i need cash on 7 aug 2020 by 5 pm,</div>');
    mainStr.push('<div>we have special previledged credit cards for your spouse, Aishwarya , whose your nominee also</div>');
    let arrContents = [];
    arrContents.push('<div style="margin-top:1rem;"></div>');
    arrContents.push(mainStr.join(''));
    contentData.innerHTML = arrContents.join('');
}


const speechUtteranceChunker = function (utt, settings, callback) {
    settings = settings || {};
    var newUtt;
    var txt = (settings && settings.offset !== undefined ? utt.text.substring(settings.offset) : utt.text);
    if (utt.voice && utt.voice.voiceURI === 'native') { // Not part of the spec
        newUtt = utt;
        newUtt.text = txt;
        newUtt.addEventListener('end', function () {
            if (speechUtteranceChunker.cancel) {
                speechUtteranceChunker.cancel = false;
            }
            if (callback !== undefined) {
                callback();
            }
        });
    } else {
        var chunkLength = (settings && settings.chunkLength) || 160;
        var pattRegex = new RegExp('^[\\s\\S]{' + Math.floor(chunkLength / 2) + ',' + chunkLength + '}[.!?,]{1}|^[\\s\\S]{1,' + chunkLength + '}$|^[\\s\\S]{1,' + chunkLength + '} ');
        var chunkArr = txt.match(pattRegex);

        if (chunkArr[0] === undefined || chunkArr[0].length <= 2) {
            //call once all text has been spoken...
            if (callback !== undefined) {
                callback();
            }
            return;
        }
        var chunk = chunkArr[0];
        newUtt = new SpeechSynthesisUtterance(chunk);
        var x;
        for (x in utt) {
            if (utt.hasOwnProperty(x) && x !== 'text') {
                newUtt[x] = utt[x];
            }
        }
        newUtt.addEventListener('end', function () {
            if (speechUtteranceChunker.cancel) {
                speechUtteranceChunker.cancel = false;
                return;
            }
            settings.offset = settings.offset || 0;
            settings.offset += chunk.length - 1;
            speechUtteranceChunker(utt, settings, callback);
        });
    }

    if (settings.modifier) {
        settings.modifier(newUtt);
    }
    console.log(newUtt); //IMPORTANT!! Do not remove: Logging the object out fixes some onend firing issues.
    //placing the speak invocation inside a callback fixes ordering and onend issues.
    setTimeout(function () {
        speechSynthesis.speak(newUtt);
    }, 0);
};
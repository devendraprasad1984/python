import urllib3
url = "https://www.google.com/speech-api/v1/recognize?xjerr=1&client=chromium&lang=en-US"
audio = open('rainspain.flac','rb').read()
headers={'Content-Type': 'audio/x-flac; rate=16000', 'User-Agent':'Mozilla/5.0'}
request = urllib3.Request(url, data=audio, headers=headers)
response = urllib3.urlopen(request)
print(response.read())

# $ python speech.py
# {"status":0,"id":"57d2d1a7e7f1fa12d200026dde946c34-1","hypotheses":[{"utterance":"the rain in Spain falls mainly on the plains","confidence":0.8385102}]}
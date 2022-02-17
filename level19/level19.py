import requests
import base64
import wave

url = 'http://www.pythonchallenge.com/pc/hex/bin.html'
data = requests.get(url, auth=('butter', 'fly')).text.split('base64\n\n')[1]
data_code = base64.b64decode(data)

with open('indian.wav', 'wb') as wav:
    wav.write(data_code)

with wave.open('indian.wav', 'rb') as wav_read:
    with wave.open('new_indian.wav', 'wb') as wav_write:
        wav_write.setparams(wav_read.getparams())
        for i in range(wav_read.getparams()[3]):
            wav_write.writeframes(wav_read.readframes(i)[::-1])
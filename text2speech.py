import os
import requests
import time
from playsound import playsound
from xml.etree import ElementTree
import requests
import json
class TextToSpeech(object):
    def __init__(self, subscription_key, color, article):
        #start weather
        api_key = "fa95a0b10d0af6aa790307ed051577b8"
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        city_name = "McLean" #input("Enter city name : ")
        #complete_url = base_url + "appid=" + api_key + "&q=" + city_name
        complete_url="http://api.openweathermap.org/data/2.5/forecast?q="
        complete_url+=city_name
        complete_url+="&APPID="
        complete_url+=api_key
        response = requests.get(complete_url)
        x = response.json()
        if x["cod"] != "404":
            y = x["list"]
            #print(y)
            temp1 = y[1]['main']['temp']
            #print(temp1)
            temp = ((temp1 - 273.15)*1.8)+33.8
            print(temp)
            raining=y[0]['weather'][0]['main']
            print(raining)
        rain=False
        if raining=='Rain':
            rain = True
        #end weather
        self.subscription_key = subscription_key
        if(color == "none"):
            self.tts = "what article of clothing would you like a suggestion for?"
        else:
            self.tts = color + " will go well with that " + article+"...................."
            if temp<40:
                self.tts +="It is very cold outside, grab a thick jacket"
            elif temp<63:
                self.tts +="looks like it's a bit chilly outside, grab a jacket"
            elif temp>=73:
                self.tts +="It is nice and sunny outside, enjoy your day"
            if rain:
                self.tts +="...................."+"It's supposed to rain in your area, grab an umbrella"
        self.timestr = time.strftime("%Y%m%d-%H%M")
        self.access_token = None
    def get_token(self):
        fetch_token_url = "https://westus.api.cognitive.microsoft.com/sts/v1.0/issueToken"
        headers = {
            'Ocp-Apim-Subscription-Key': self.subscription_key
        }
        response = requests.post(fetch_token_url, headers=headers)
        self.access_token = str(response.text)

    def save_audio(self, name):
        base_url = 'https://westus.tts.speech.microsoft.com/'
        path = 'cognitiveservices/v1'
        constructed_url = base_url + path
        headers = {
            'Authorization': 'Bearer ' + self.access_token,
            'Content-Type': 'application/ssml+xml',
            'X-Microsoft-OutputFormat': 'riff-24khz-16bit-mono-pcm',
            'User-Agent': 'text2speeches'
        }
        xml_body = ElementTree.Element('speak', version='1.0')
        xml_body.set('{http://www.w3.org/XML/1998/namespace}lang', 'en-us')
        voice = ElementTree.SubElement(xml_body, 'voice')
        voice.set('{http://www.w3.org/XML/1998/namespace}lang', 'en-US')
        voice.set(
            'name', 'Microsoft Server Speech Text to Speech Voice (en-US, Guy24KRUS)')
        voice.text = self.tts
        body = ElementTree.tostring(xml_body)

        response = requests.post(constructed_url, headers=headers, data=body)
        if response.status_code == 200:
            with open(name, 'wb') as audio:
                audio.write(response.content)
                print("\nStatus code: " + str(response.status_code) +
                      "\nYour TTS is ready for playback.\n")
        else:
            print("\nStatus code: " + str(response.status_code) +
                  "\nSomething went wrong. Check your subscription key and headers.\n")
if __name__ == "__main__":
    subscription_key = "3dcb81c95f9d46248813f574677f3272"
    app = TextToSpeech(subscription_key)
    app.get_token()
    app.save_audio()
    playsound('sample.wav')
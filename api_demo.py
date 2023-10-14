# to import the subscription_key
from settings import key

# Use the requests library to simplify making a REST API call from Python
import requests

# We will need the json library to read the data passed back by the web service
import json

# address of the service giver
# you should sign up on rapidapi.com and subscribe for the google translate api on "https://rapidapi.com/googlecloud/api/google-translate1/"
# you can subscribe for a plan that is suitable for you
request_url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

# setting up  headers according to the documentation of the API
headers = {
    "content-type": "application/x-www-form-urlencoded",
    "Accept-Encoding": "application/gzip",
    "X-RapidAPI-Key": key,
    "X-RapidAPI-Host": "google-translate1.p.rapidapi.com",
}

# parameters that are being passed on to the API

#Request body

# Required parameters
Quest = input("What do you want to translate?\n")
Target_language = input("What language you want to traslate it too?(eg. 'es','am')\n")
# optional parameters
#format="HTML"
# The format of the source text, in either HTML (default) or plain-text. A value of html indicates HTML and a value of text indicates plain-text

#source="en"
# The language of the source text, set to one of the language codes listed in Language Support. If the source language is not specified, the API will attempt to detect the source language automatically and return it within the response.

#setting up our data in a format
payload={
    "q":Quest,
    "target":Target_language
}

#let's translate the words to the desired language by using the API by receiving it in the form of JSON

response=requests.post(request_url,data=payload,headers=headers)

#to print out the result

print(response.json())

#to specifically print out the words that are translated
# 
data=response.json()['data']['translations'][0]['translatedText'] 
print('data')
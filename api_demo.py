#to import the subscription_key
from settings import key
#Use the requests library to simplify making a REST API call from Python
import requests
# We will need the json library to read the data passed back by the web service
import json

#address of the service giver
#you should sign up on rapidapi.com and subscribe for the google translate api on "https://rapidapi.com/googlecloud/api/google-translate1/"
#you can subscribe for a plan that is suitable for you
request_url="https://google-translate1.p.rapidapi.com/language/translate/v2"

#setting up  headers according to the documentation of the API
headers={
    "content-type": "application/x-www-form-urlencoded",
	"Accept-Encoding": "application/gzip",
    "X-RapidAPI-Key":key,
    "X-RapidAPI-Host":"google-translate1.p.rapidapi.com"
}

#parameters that are being passed on to the API
Quest=input("What do you want to translate?")
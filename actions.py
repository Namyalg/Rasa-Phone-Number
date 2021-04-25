# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from weather import Weather
import requests
import json

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_weather_api"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        city = tracker.latest_message['text']
        #temp=int(Weather(city)['temp']-273)

        url = "https://d63af3efc483.ngrok.io/" + str(city)       
        
        resp = requests.get(url)
        

        resp = json.loads(resp.text)
        pt = (resp["Present"])

        dispatcher.utter_message(text=pt)
        #dispatcher.utter_message('We did not find any weather information for. Search by a city name.')


        #dispatcher.utter_template("utter_temp",tracker,temp=temp)

        return []

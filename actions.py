from rasa_sdk import Action
from rasa_sdk.events import SlotSet


class getSpecialistAPI:
    def search(self, info):
        return "Doctor Goodbridge at High street"


class ActionSearchSpecialist(Action):
    def name(self):
        return "action_search_specialist"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(text="looking for specialist")
        FindSpecialist_api = getSpecialistAPI()
        specialists = FindSpecialist_api.search(tracker.get_slot("Specialist"))
        return [SlotSet("matches", specialists)]


class ActionRecommend(Action):
    def name(self):
        return "action_recommend"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(text="here's the specialist I found:")
        dispatcher.utter_message(text=tracker.get_slot("matches"))
        dispatcher.utter_message(
            text="I hope you make an appointment there asap"
        )
        return []

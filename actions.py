from rasa_sdk import Action
from rasa_sdk.events import SlotSet


class get_specialistAPI:
    def search(self, info):
        return "Doctor Goodbridge at High street"


class Action_searchSpecialist(Action):
    def name(self):
        return "action_searchSpecialist"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(text="looking for specialist")
        FindSpecialist_api = get_specialistAPI()
        specialists = FindSpecialist_api.search(tracker.get_slot("Specialist"))
        return [SlotSet("matches", specialists)]


class Action_Recommend(Action):
    def name(self):
        return "action_recommend"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(text="here's the specialist I found:")
        dispatcher.utter_message(text=tracker.get_slot("matches"))
        dispatcher.utter_message(
            text="I hope you make an appointment there asap"
        )
        return []


## interactive_story_1
* intent_askSeeDoctor
    - utter_askHasAppointment
* intent_denyHaveAppointment
    - utter_askMakeAppointment
* intent_denyHaveAppointment
    - utter_tellCantHelp
* intent_agreeTo
    - utter_goodbye
* intent_goodbye


## interactive_story_1
* intent_greet
    - utter_greet
    - utter_askSymptom
* intent_tellSymptom{"SymptomName": "fever"}
    - slot{"SymptomName": "fever"}
    - utter_acknowledge
    - utter_askWhatElse
* intent_denyHaveAppointment
    - utter_askSymptomDuration
* intent_tellSymptom{"SymptomDuration": "days"}
    - slot{"SymptomDuration": "days"}
    - utter_tellDiagnosis
    - utter_tellPrescription
* intent_thank
    - utter_goodbye
* intent_goodbye
    - action_restart

## interactive_story_2
* intent_greet
    - utter_greet
    - utter_askSymptom
* intent_tellSymptom{"SymptomName": "temperature"}
    - slot{"SymptomName": "temperature"}
    - utter_acknowledge
    - utter_askWhatElse
* intent_agreeTo
* intent_tellSymptom{"SymptomName": "fever"}
    - slot{"SymptomName": "fever"}
    - utter_askSymptomDuration
* intent_tellSymptom{"SymptomDuration": "months"}
    - slot{"SymptomDuration": "months"}
    - action_searchSpecialist
    - action_recommend
* intent_agreeTo
    - action_recommend

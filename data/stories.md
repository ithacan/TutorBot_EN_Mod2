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

## New Story

* intent_greet
    - utter_greet
    - utter_askSymptom
* intent_askSeeDoctor
    - utter_askHasAppointment
* intent_denyHaveAppointment
    - utter_askMakeAppointment
* intent_agreeTo
    - utter_askAppointmentTomorrow
* intent_askSeeDoctor
    - utter_askAppointmentFriday
* intent_agreeTo
    - utter_tellMadeAppointment
* intent_thank
    - utter_goodbye
* intent_goodbye
    - utter_goodbye

## New Story

* intent_greet
    - utter_greet
    - utter_askSymptom
* intent_askSeeDoctor
    - utter_askHasAppointment
* intent_agreeTo
    - utter_askName
* intent_tellName{"PatientName":"John Doe"}
    - slot{"PatientName":"John Doe"}
    - slot{"PatientName":"John Doe"}
    - utter_utter_tellFoundAppointment
* intent_thank
    - slot{"PatientName":"John Doe"}
    - utter_utter_thanks

## New Story

* intent_greet
    - utter_greet
    - utter_askSymptom
* intent_askSeeDoctor
    - utter_askHasAppointment
* intent_denyHaveAppointment
    - utter_askMakeAppointment
* intent_agreeTo
    - utter_askAppointmentTomorrow
* intent_agreeTo
    - utter_askChooseTime
* intent_sayTwoPM
    - utter_tellMadeAppointment
* intent_thank
    - utter_goodbye

## New Story

* intent_greet
    - utter_greet
    - utter_askSymptom
* intent_askSeeDoctor
    - utter_askHasAppointment
* intent_denyHaveAppointment
    - utter_askMakeAppointment
* intent_agreeTo
    - utter_askName
* intent_askSeeDoctor{"PatientName":"James"}
    - slot{"PatientName":"James"}
    - slot{"PatientName":"James"}
    - utter_askAppointmentTomorrow
* intent_agreeTo
    - slot{"PatientName":"James"}
    - utter_askChooseTime
* intent_sayTwoPM
    - slot{"PatientName":"James"}
    - utter_tellMadeAppointment
* intent_thank
    - utter_goodbye

## New Story

* intent_greet
    - utter_greet
    - utter_askSymptom
* intent_tellSymptom{"SymptomName":"fever"}
    - slot{"SymptomName":"fever"}
    - slot{"SymptomName":"fever"}
    - utter_acknowledge
    - utter_askWhatElse
* intent_agreeTo
* intent_tellSymptom{"SymptomName":"sweaty palms"}
    - slot{"SymptomName":"sweaty palms"}
    - slot{"SymptomName":"sweaty palms"}
    - utter_askSymptomDuration
* intent_tellSymptom{"SymptomDuration":"years"}
    - slot{"SymptomDuration":"years"}
    - slot{"SymptomDuration":"years"}
    - action_searchSpecialist
    - slot{"matches":"Doctor Goodbridge at High street"}
    - action_recommend
* intent_agreeTo
    - slot{"SymptomName":"fever"}
    - slot{"SymptomName":"sweaty palms"}
    - slot{"SymptomDuration":"years"}
    - utter_tellReferral
* intent_agreeTo
    - utter_goodbye
* intent_goodbye
    - action_default_fallback

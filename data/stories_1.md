## story_Hospital_DoctorInterview_1_A
* intent_greet
 - utter_greet
 - utter_askSymptom
* intent_tellSymptom{"SymptomName": "high temperature"}
 - utter_acknowledge
 - utter_askWhatElse
* intent_affirm
 - utter_sayGoOn
* intent_tellSymptom{"SymptomName": "fever"}
 - utter_askSymptomDuration
* intent_tellSymptom{"SymptomDuartion": "2 days"}
 - utter_tellDiagnosis
 - utter_tellPrescription
* intent_thank
 - utter_goodbye

## story_Hospital_DoctorInterview_1_B
* intent_greet
 - utter_greet
 - utter_askSymptom
* intent_tellSymptom{"SymptomName": "high temperature"}
 - utter_acknowledge
 - utter_askWhatElse
* intent_deny
 - utter_askSymptomDuration
* intent_tellSymptom{"SymptomDuartion": "2 days"}
 - utter_tellDiagnosis
 - utter_tellPrescription
* intent_thank
 - utter_goodbye

## interactive_story_1_C
* intent_greet
    - utter_greet
    - utter_askSymptom
* intent_tellSymptom{"SymptomName": "dry mouth"}
    - slot{"SymptomName": "dry mouth"}
    - utter_acknowledge
    - utter_askWhatElse
* intent_deny
    - utter_askSymptomDuration
* intent_tellSymptom{"SymptomDuration": "days"}
    - slot{"SymptomDuration": "days"}
    - utter_tellDiagnosis
    - utter_tellPrescription
* intent_affirm
    - utter_goodbye
* intent_goodbye

## interactive_story_1_D
* intent_greet
    - utter_greet
    - utter_askSymptom
* intent_tellSymptom{"SymptomName": "stomach ache"}
    - slot{"SymptomName": "stomach ache"}
    - utter_acknowledge
    - utter_askWhatElse
* intent_affirm
    - utter_sayGoOn
* intent_tellSymptom{"SymptomName": "fever"}
    - slot{"SymptomName": "fever"}
    - utter_askSymptomDuration
* intent_tellSymptom{"SymptomDuration": "months"}
    - slot{"SymptomDuration": "months"}
    - utter_tellDiagnosis
    - utter_tellPrescription
* intent_affirm
    - utter_goodbye
* intent_goodbye

## story_Hospital_DoctorInterview_1_E
* intent_greet
 - utter_greet
 - utter_askSymptom
* intent_tellSymptom{"SymptomName": "high temperature"}
 - utter_acknowledge
 - utter_askWhatElse
* intent_affirm
 - utter_sayGoOn
* intent_tellSymptom{"SymptomName": "fever"}
 - utter_askSymptomDuration
* intent_tellSymptom{"SymptomDuartion": "2 days"}
 - utter_tellDiagnosis
 - utter_tellReferral
* intent_affirm
 - action_searchSpecialist
 - action_recommend
* intent_thank
 - utter_goodbye

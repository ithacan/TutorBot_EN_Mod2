## story_Dialog_1_A
* tell_Greet
 - utter_say_Greet
 - utter_ask_Symptom
* tell_inform{"SymptomName": "sore throat"}
 - utter_ack
 - utter_ask_WhatElse
* tell_inform{"SymptomName": "high temperature"}
 - utter_ask_SymptomDuration
* tell_inform{"SymptomDuartion": "2 days"}
 - utter_say_Diagnosis
 - utter_say_Prescription
* tell_Thanks
 - utter_say_Goodbye

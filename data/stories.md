## story_Dialog_1_A
* tell_Greet
 - utter_say_Greet
 - utter_ask_Symptom
* inform_Symptom{"SymptomName": "high temperature"}
 - utter_ack
 - utter_ask_WhatElse
* tell_Affirm
 - utter_say_GoOn
* inform_Symptom{"SymptomName": "fever"}
 - utter_ask_SymptomDuration
* inform_Symptom{"SymptomDuartion": "2 days"}
 - utter_say_Diagnosis
 - utter_say_Prescription
* tell_Thanks
 - utter_say_Goodbye

## story_Dialog_1_B
* tell_Greet
 - utter_say_Greet
 - utter_ask_Symptom
* inform_Symptom{"SymptomName": "high temperature"}
 - utter_ack
 - utter_ask_WhatElse
* tell_Deny
 - utter_ask_SymptomDuration
* inform_Symptom{"SymptomDuartion": "2 days"}
 - utter_say_Diagnosis
 - utter_say_Prescription
* tell_Thanks
 - utter_say_Goodbye

## interactive_story_1_C
* tell_Greet
    - utter_say_Greet
    - utter_ask_Symptom
* inform_Symptom{"SymptomName": "dry mouth"}
    - slot{"SymptomName": "dry mouth"}
    - utter_ack
    - utter_ask_WhatElse
* tell_Deny
    - utter_ask_SymptomDuration
* inform_Symptom{"SymptomDuration": "days"}
    - slot{"SymptomDuration": "days"}
    - utter_say_Diagnosis
    - utter_say_Prescription
* tell_Affirm
    - utter_say_Goodbye
* tell_Goodbye

## interactive_story_1_D
* tell_Greet
    - utter_say_Greet
    - utter_ask_Symptom
* inform_Symptom{"SymptomName": "stomach ache"}
    - slot{"SymptomName": "stomach ache"}
    - utter_ack
    - utter_ask_WhatElse
* tell_Affirm
    - utter_say_GoOn
* inform_Symptom{"SymptomName": "fever"}
    - slot{"SymptomName": "fever"}
    - utter_ask_SymptomDuration
* inform_Symptom{"SymptomDuration": "months"}
    - slot{"SymptomDuration": "months"}
    - utter_say_Diagnosis
    - utter_say_Prescription
* tell_Affirm
    - utter_say_Goodbye
* tell_Goodbye

## story_Dialog_1_E
* tell_Greet
 - utter_say_Greet
 - utter_ask_Symptom
* inform_Symptom{"SymptomName": "high temperature"}
 - utter_ack
 - utter_ask_WhatElse
* tell_Affirm
 - utter_say_GoOn
* inform_Symptom{"SymptomName": "fever"}
 - utter_ask_SymptomDuration
* inform_Symptom{"SymptomDuartion": "2 days"}
 - utter_say_Diagnosis
 - utter_say_Referral
* tell_Affirm
 - action_search_specialist
 - action_recommend
* tell_Thanks
 - utter_say_Goodbye

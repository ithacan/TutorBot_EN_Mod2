## story_Hospital_MakeAppointment_2_A
* intent_askSeeDoctor
> 2A1
> 2A1
 - utter_askHasAppointment
> 2A2
> 2A2
* intent_denyHaveAppointment
> 2A3
> 2A3
 - utter_askMakeAppointment
> 2A4
> 2A4
* intent_agreeTo
> 2A5
> 2A5
 - utter_askName
> 2A6
> 2A6
* intent_tellName
> 2A7
> 2A7
 - utter_askAppointmentTomorrow
> 2A8
> 2A8
* intent_affirm
> 2A9
> 2A9
- utter_tellMadeAppointment
> 2A11
> 2A11
* intent_thank
> 2A12
> 2A12
 - utter_goodbye
> 2A13
> 2A13
* intent_goodbye
- action_restart

## interactive_story_2_B
* intent_askSeeDoctor
    - utter_askHasAppointment
* intent_denyHaveAppointment
    - utter_askMakeAppointment
* intent_agreeTo
    - utter_askName
* intent_tellName{"PatientName": "John Doe"}
    - slot{"PatientName": "John Doe"}
    - utter_askAppointmentTomorrow
* intent_agreeTo
    - utter_tellMadeAppointment
* intent_thank
    - utter_goodbye
* intent_goodbye

## interactive_story_2_C
* intent_askSeeDoctor
    - utter_askHasAppointment
* intent_denyHaveAppointment
    - utter_askMakeAppointment
* intent_deny
    - utter_tellCantHelp
* intent_affirm OR intent_agreeTo OR intent_goodbye
    - utter_goodbye


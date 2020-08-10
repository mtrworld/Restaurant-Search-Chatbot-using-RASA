## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bengaluru"}
    - slot{"location": "bengaluru"}
    - action_verify_location
    - slot{"location": "bengaluru"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budgetmin": "300", "budgetmax": "700"}
    - slot{"budgetmax": "700"}
    - slot{"budgetmin": "300"}
    - action_search_restaurants
    - slot{"location": "bengaluru"}
    - slot{"restaurant_exist": true}
* affirm
    - utter_ask_email
* send_mail
    - utter_ask_emailid
* send_mail{"emailid": "mtrworld@gmail.com"}
    - slot{"emailid": "mtrworld@gmail.com"}
    - action_verify_email
    - slot{"emailid": "mtrworld@gmail.com"}
	- slot{"email_ok": true}
    - action_send_email
    - utter_ask_howcanhelp
* deny{"deny": "No"}
    - utter_goodbye
	- action_restarted


## interactive_story_2
* greet
    - utter_greet
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_verify_location
    - slot{"location": null}
    - slot{"location_ok": false}
* restaurant_search{"location": "Allahabad"}
    - slot{"location": "Allahabad"}
    - action_verify_location
    - slot{"location": "Allahabad"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budgetmin": "300", "budgetmax": "700"}
    - slot{"budgetmax": "700"}
    - slot{"budgetmin": "300"}
    - action_search_restaurants
    - slot{"location": "Allahabad"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* send_mail
    - utter_ask_email
    - utter_ask_emailid
* send_mail{"emailid": "mudassar.iiita@gmail.com"}
    - slot{"emailid": "mudassar.iiita@gmail.com"}
	- action_verify_email
    - slot{"emailid": "mudassar.iiita@gmail.com"}
	- slot{"email_ok": true}
    - action_send_email
    - utter_ask_howcanhelp
* deny{"deny": "No"}
    - utter_goodbye
	- action_restarted

## interactive_story_3
* greet
    - utter_greet
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
    - action_verify_location
    - slot{"location": "Kolkata"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_budget
* restaurant_search{"budgetmin": "0", "budgetmax": "300"}
    - slot{"budgetmax": "300"}
    - slot{"budgetmin": "0"}
    - action_search_restaurants
    - slot{"location": "Kolkata"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* send_mail
    - utter_ask_emailid
* send_mail{"emailid": "jddk.2jmd@kdl.co.in"}
    - slot{"emailid": "jddk.2jmd@kdl.co.in"}
	- action_verify_email
    - slot{"emailid": "jddk.2jmd@kdl.co.in"}
	- slot{"email_ok": true}
    - action_send_email
    - utter_ask_howcanhelp
* deny{"deny": "No"}
    - utter_goodbye
	- action_restarted

## interactive_story_4
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mubaim"}
    - slot{"location": "mubaim"}
    - action_verify_location
    - slot{"location": null}
    - slot{"location_ok": false}
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_verify_location
    - slot{"location": "Mumbai"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_budget
* restaurant_search{"budgetmin": "0", "budgetmax": "300"}
    - slot{"budgetmax": "300"}
    - slot{"budgetmin": "0"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* send_mail
    - utter_ask_emailid
* send_mail{"emailid": "jddk.2mjd@kdl.co.in"}
    - slot{"emailid": "jddk.2mjd@kdl.co.in"}
	- action_verify_email
    - slot{"emailid": "jddk.2mjd@kdl.co.in"}
	- slot{"email_ok": true}
    - action_send_email
    - utter_ask_howcanhelp
* deny
    - utter_goodbye
	- action_restarted

## interactive_story_5
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Chandigarh"}
    - action_verify_location
    - slot{"location": "Chandigarh"}
    - slot{"location_ok": true}
    - utter_ask_budget
* restaurant_search{"budgetmin": "0", "budgetmax": "300"}
    - slot{"budgetmax": "300"}
    - slot{"budgetmin": "0"}
    - action_search_restaurants
    - slot{"location": "Chandigarh"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* dont_send_email
    - utter_ask_howcanhelp
* deny
    - utter_goodbye
	- action_restarted

## interactive_story_6
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Bombay"}
    - slot{"location": "Bombay"}
    - action_verify_location
    - slot{"location": "Bombay"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_budget
* restaurant_search{"budgetmin": "300", "budgetmax": "700"}
    - slot{"budgetmax": "700"}
    - slot{"budgetmin": "300"}
    - action_search_restaurants
    - slot{"location": "Bombay"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* dont_send_email
	- utter_ask_howcanhelp
* deny
    - utter_goodbye
	- action_restarted

## interactive_story_7
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "bangalore"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "bangalore"}
    - action_verify_location
    - slot{"location": "bangalore"}
    - slot{"location_ok": true}
    - utter_ask_budget
* restaurant_search{"budgetmin": "300", "budgetmax": "700"}
    - slot{"budgetmax": "700"}
    - slot{"budgetmin": "300"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* dont_send_email
    - utter_ask_howcanhelp
* deny
    - utter_goodbye
	- action_restarted

## interactive_story_8
* greet
    - utter_greet
* restaurant_search{"cuisine": "thai", "location": "banglor"}
    - slot{"cuisine": "thai"}
    - slot{"location": "banglor"}
    - action_verify_location
    - slot{"location": null}
    - slot{"location_ok": false}
* restaurant_search{"location": "bangalur"}
    - slot{"location": "bangalur"}
    - action_verify_location
    - slot{"location": null}
    - slot{"location_ok": false}
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_verify_location
    - slot{"location": "bangalore"}
    - slot{"location_ok": true}
    - utter_ask_budget
* restaurant_search{"budgetmin": "700", "budgetmax": "10000"}
    - slot{"budgetmax": "10000"}
    - slot{"budgetmin": "700"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* dont_send_email
    - utter_ask_howcanhelp
* deny
    - utter_goodbye
	- action_restarted

## interactive_story_9
* greet
    - utter_greet
* restaurant_search{"location": "Hyderabad"}
    - slot{"location": "Hyderabad"}
    - action_verify_location
    - slot{"location": "Hyderabad"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_budget
* restaurant_search{"budgetmin": "300", "budgetmax": "700"}
    - slot{"budgetmax": "700"}
    - slot{"budgetmin": "300"}
    - action_search_restaurants
    - slot{"location": "Hyderabad"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* send_mail
    - utter_ask_emailid
* send_mail{"emailid": "shedoncooper@caltech.ac.in"}
    - slot{"emailid": "shedoncooper@caltech.ac.in"}
	- action_verify_email
    - slot{"emailid": "shedoncooper@caltech.ac.in"}
	- slot{"email_ok": true}
    - action_send_email
    - utter_ask_howcanhelp
* deny
    - utter_goodbye
	- action_restarted

## interactive_story_10
* greet
    - utter_greet
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_verify_location
    - slot{"location": "Delhi"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_budget
* restaurant_search{"budgetmin": "300", "budgetmax": "700"}
    - slot{"budgetmax": "700"}
    - slot{"budgetmin": "300"}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* dont_send_email
    - utter_ask_howcanhelp
* deny
    - utter_goodbye
	- action_restarted

## interactive_story_11
* restaurant_search{"cuisine": "amerika", "location": "Pune"}
    - slot{"cuisine": "amerika"}
    - slot{"location": "Pune"}
    - action_verify_location
    - slot{"location": "Pune"}
    - slot{"location_ok": true}
    - utter_ask_budget
* restaurant_search{"budgetmin": "300", "budgetmax": "700"}
    - slot{"budgetmax": "700"}
    - slot{"budgetmin": "300"}
    - action_search_restaurants
    - slot{"location": "Pune"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* send_mail
    - utter_ask_emailid
* send_mail{"emailid": "mtrworld@gmail.com"}
    - slot{"emailid": "mtrworld@gmail.com"}
	- slot{"email_ok": true}
    - action_send_email
    - utter_ask_howcanhelp
* deny
    - utter_goodbye
	- action_restarted

## interactive_story_12
* greet
    - utter_greet
* restaurant_search{"location": "near"}
    - slot{"location": "near"}
    - action_verify_location
    - slot{"location": null}
    - slot{"location_ok": false}
* restaurant_search{"location": "mubaim"}
    - slot{"location": "mubaim"}
    - action_verify_location
    - slot{"location": null}
    - slot{"location_ok": false}
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_verify_location
    - slot{"location": "Mumbai"}
    - slot{"location_ok": true}
    - utter_ask_budget
* restaurant_search{"budgetmin": "300", "budgetmax": "700"}
    - slot{"budgetmax": "700"}
    - slot{"budgetmin": "300"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* dont_send_email
    - utter_ask_howcanhelp
* deny
    - utter_goodbye
	- action_restarted

## interactive_story_13
* greet
    - utter_greet
* restaurant_search{"location": "560017"}
    - slot{"location": "560017"}
    - action_verify_location
    - slot{"location": null}
    - slot{"location_ok": false}
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_verify_location
    - slot{"location": "bangalore"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_budget
* restaurant_search{"budgetmin": "300", "budgetmax": "700"}
    - slot{"budgetmax": "700"}
    - slot{"budgetmin": "300"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* dont_send_email
    - utter_ask_howcanhelp
* deny
    - utter_goodbye
	- action_restarted

## interactive_story_14
* greet
    - utter_greet
* restaurant_search{"location": "415612"}
    - slot{"location": "415612"}
    - action_verify_location
    - slot{"location": null}
    - slot{"location_ok": false}
* restaurant_search{"location": "ratnagiri"}
    - slot{"location": "ratnagiri"}
    - action_verify_location
    - slot{"location": null}
    - slot{"location_ok": false}
* restaurant_search{"location": "Raipur"}
    - slot{"location": "Raipur"}
    - action_verify_location
    - slot{"location": "Raipur"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_budget
* restaurant_search{"budgetmin": "300", "budgetmax": "700"}
    - slot{"budgetmax": "700"}
    - slot{"budgetmin": "300"}
    - action_search_restaurants
    - slot{"location": "Raipur"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* dont_send_email
    - utter_ask_howcanhelp
* deny
    - utter_goodbye
	- action_restarted

## interactive_story_15
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_verify_location
    - slot{"location": "Mumbai"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budgetmin": "300", "budgetmax": "700"}
    - slot{"budgetmax": "700"}
    - slot{"budgetmin": "300"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* dont_send_email
    - utter_ask_howcanhelp
* deny
    - utter_goodbye
	- action_restarted

## interactive_story_16
* greet
    - utter_greet
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_verify_location
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budgetmin": "0", "budgetmax": "300"}
    - slot{"budgetmax": "300"}
    - slot{"budgetmin": "0"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* dont_send_email
    - utter_ask_howcanhelp
* deny
    - utter_goodbye
	- action_restarted

## interactive_story_17
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "bangalore"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "bangalore"}
    - action_verify_location
    - slot{"location": "bangalore"}
    - slot{"location_ok": true}
    - utter_ask_budget
* restaurant_search{"budgetmin": "300", "budgetmax": "700"}
    - slot{"budgetmax": "700"}
    - slot{"budgetmin": "300"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* send_mail
    - utter_ask_emailid
* send_mail{"emailid": "mtrworld"}
    - slot{"emailid": "mtrworld"}
    - action_verify_email
    - slot{"emailid": null}
    - slot{"email_ok": false}
* send_mail{"emailid": "mtrworld@gmail"}
    - slot{"emailid": "mtrworld@gmail"}
    - action_verify_email
    - slot{"emailid": null}
    - slot{"email_ok": false}
* send_mail{"emailid": "mtrworld.com"}
    - slot{"emailid": "mtrworld.com"}
    - action_verify_email
    - slot{"emailid": null}
    - slot{"email_ok": false}
* send_mail{"emailid": "mtrworld@gmail.com"}
    - slot{"emailid": "mtrworld@gmail.com"}
    - action_verify_email
    - slot{"emailid": "mtrworld@gmail.com"}
	- slot{"email_ok": true}
    - action_send_email
    - utter_ask_howcanhelp
* deny{"deny": "No"}
    - utter_goodbye
	- action_restarted

## interactive_story_18
* greet
    - utter_greet
* restaurant_search{"cuisine": "north indian", "location": "bangalore"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "bangalore"}
    - action_verify_location
    - slot{"location": "bangalore"}
    - slot{"location_ok": true}
    - utter_ask_budget
* restaurant_search{"budgetmin": "500", "budgetmax": "1000"}
    - slot{"budgetmax": "1000"}
    - slot{"budgetmin": "500"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* send_mail
    - utter_ask_emailid
* send_mail{"emailid": "2fun2cool@fake.id"}
    - slot{"emailid": "2fun2cool@fake.id"}
    - action_verify_email
    - slot{"emailid": "2fun2cool@fake.id"}
	- slot{"email_ok": true}
    - action_send_email
    - utter_ask_howcanhelp
* deny
    - utter_goodbye
	- action_restarted

## interactive_story_19
* greet
    - utter_greet
* restaurant_search{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - utter_ask_location
* restaurant_search{"location": "Chandigarh"}
    - slot{"location": "Chandigarh"}
    - action_verify_location
    - slot{"location": "Chandigarh"}
    - slot{"location_ok": true}
    - utter_ask_budget
* restaurant_search{"budgetmin": "0", "budgetmax": "300"}
    - slot{"budgetmax": "300"}
    - slot{"budgetmin": "0"}
    - action_search_restaurants
    - slot{"location": "Chandigarh"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* send_mail
    - utter_ask_emailid
* restaurant_search{"emailid": "rajkutrapali123@india.in"}
    - slot{"emailid": "rajkutrapali123@india.in"}
    - action_verify_email
    - slot{"emailid": "rajkutrapali123@india.in"}
	- slot{"email_ok": true}
    - action_send_email
    - utter_ask_howcanhelp
* deny
    - utter_goodbye
	- action_restarted

## interactive_story_20
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_location
* restaurant_search{"location": "mexico"}
    - slot{"location": "mexico"}
    - action_verify_location
    - slot{"location": null}
    - slot{"location_ok": false}
* restaurant_search{"location": "Chennai"}
    - slot{"location": "Chennai"}
    - action_verify_location
    - slot{"location": "Chennai"}
    - slot{"location_ok": true}
    - utter_ask_budget
* restaurant_search{"budgetmax": "1000", "budgetmin": "500"}
    - slot{"budgetmax": "1000"}
    - slot{"budgetmin": "500"}
    - action_search_restaurants
    - slot{"location": "Chennai"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* send_mail
    - utter_ask_emailid
* send_mail{"emailid": "howard-wolowitz@mexicon.ai"}
    - slot{"emailid": "howard-wolowitz@mexicon.ai"}
    - action_verify_email
    - slot{"emailid": "howard-wolowitz@mexicon.ai"}
	- slot{"email_ok": true}
    - action_send_email
    - utter_ask_howcanhelp
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_location
* restaurant_search
    - utter_ask_budget
* restaurant_search
    - action_search_restaurants
    - slot{"location": "Chennai"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* dont_send_email
    - utter_ask_howcanhelp
* deny{"deny": "Thats it"}
    - utter_goodbye
	- action_restarted

## interactive_story_21
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "bangalore"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "bangalore"}
    - action_verify_location
    - slot{"location": "bangalore"}
    - slot{"location_ok": true}
    - utter_ask_budget
* restaurant_search{"budgetmin": "0", "budgetmax": "300"}
    - slot{"budgetmax": "300"}
    - slot{"budgetmin": "0"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* send_mail
    - utter_ask_emailid
* send_mail{"emailid": "bernie_rotowsinki_wolwowitz@micro.mi"}
    - slot{"emailid": "bernie_rotowsinki_wolwowitz@micro.mi"}
    - action_verify_email
    - slot{"emailid": "bernie_rotowsinki_wolwowitz@micro.mi"}
	- slot{"email_ok": true}
    - action_send_email
    - utter_ask_howcanhelp
* deny{"deny": "No"}
    - utter_goodbye
	- action_restarted

## interactive_story_22
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Jabalpur"}
    - slot{"location": "Jabalpur"}
    - action_verify_location
    - slot{"location": "Jabalpur"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget
* restaurant_search{"budgetmin": "300", "budgetmax": "700"}
    - slot{"budgetmax": "700"}
    - slot{"budgetmin": "300"}
    - action_search_restaurants
    - slot{"location": "Jabalpur"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* send_mail
    - utter_ask_emailid
* send_mail{"emailid": "amy?farafowler@gmail.com"}
    - slot{"emailid": "amy?farafowler@gmail.com"}
    - action_verify_email
    - slot{"emailid": null}
    - slot{"email_ok": false}
* send_mail{"emailid": "amy/farafowler@gmail.com"}
    - slot{"emailid": "amy/farafowler@gmail.com"}
    - action_verify_email
    - slot{"emailid": null}
    - slot{"email_ok": false}
* send_mail{"emailid": "amyfarafowler@gmail.com"}
    - slot{"emailid": "amyfarafowler@gmail.com"}
    - action_verify_email
    - slot{"emailid": "amyfarafowler@gmail.com"}
	- slot{"email_ok": true}
    - action_send_email
    - utter_ask_howcanhelp
* deny{"deny": "No"}
    - utter_goodbye
	- action_restarted

## interactive_story_23
* greet
    - utter_greet
* restaurant_search{"location": "Rajkot"}
    - slot{"location": "Rajkot"}
    - action_verify_location
    - slot{"location": "Rajkot"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_budget
* restaurant_search{"budgetmin": "300", "budgetmax": "700"}
    - slot{"budgetmax": "700"}
    - slot{"budgetmin": "300"}
    - action_search_restaurants
    - slot{"location": "Rajkot"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* send_mail
    - utter_ask_emailid
* restaurant_search{"emailid": "?pennyh@two.in"}
    - slot{"emailid": "?pennyh@two.in"}
    - action_verify_email
    - slot{"emailid": null}
    - slot{"email_ok": false}
* send_mail{"emailid": "pennyh@two.in"}
    - slot{"emailid": "pennyh@two.in"}
    - action_verify_email
    - slot{"emailid": "pennyh@two.in"}
	- slot{"email_ok": true}
    - action_send_email
    - utter_ask_howcanhelp
* deny
    - utter_goodbye
	- action_restarted

## interactive_story_24
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Shimla"}
    - slot{"location": "Shimla"}
    - action_verify_location
    - slot{"location": "Shimla"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_budget
* restaurant_search{"budgetmin": "700", "budgetmax": "10000"}
    - slot{"budgetmax": "10000"}
    - slot{"budgetmin": "700"}
    - action_search_restaurants
    - utter_ask_email
* send_mail{"send_mail": "Yes send", "emailid": "mtrdosa@gmail.com"}
    - slot{"emailid": "mtrdosa@gmail.com"}
    - action_verify_email
    - slot{"emailid": "mtrdosa@gmail.com"}
    - slot{"email_ok": true}
    - action_send_email
    - utter_ask_howcanhelp
* deny
    - utter_goodbye
	- action_restarted

## interactive_story_25
* greet
    - utter_greet
* restaurant_search{"location": "Bokaro Steel City"}
    - slot{"location": "Bokaro Steel City"}
    - action_verify_location
    - slot{"location": "Bokaro Steel City"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget
* restaurant_search{"budgetmin": "700", "budgetmax": "10000"}
    - slot{"budgetmax": "10000"}
    - slot{"budgetmin": "700"}
    - action_search_restaurants
    - slot{"location": "Bokaro Steel City"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* send_mail
    - utter_ask_emailid
* send_mail{"emailid": "?staurt/comic@bookstore.com"}
    - slot{"emailid": "?staurt/comic@bookstore.com"}
    - action_verify_email
    - slot{"emailid": null}
    - slot{"email_ok": false}
* send_mail{"emailid": "stuart123comic@bookstore.com"}
    - slot{"emailid": "stuart123comic@bookstore.com"}
    - action_verify_email
    - slot{"emailid": "stuart123comic@bookstore.com"}
    - slot{"email_ok": true}
    - action_send_email
    - utter_ask_howcanhelp
* deny
    - utter_goodbye
	- action_restarted

## interactive_story_26
* greet
    - utter_greet
* restaurant_search{"location": "Ooty"}
    - slot{"location": "Ooty"}
    - action_verify_location
    - slot{"location": null}
    - slot{"location_ok": false}
* restaurant_search{"location": "Coorg"}
    - slot{"location": "Coorg"}
    - action_verify_location
    - slot{"location": null}
    - slot{"location_ok": false}
* restaurant_search{"location": "Kullu"}
    - slot{"location": "Kullu"}
    - action_verify_location
    - slot{"location": null}
    - slot{"location_ok": false}
* restaurant_search{"location": "Manali"}
    - slot{"location": "Manali"}
    - action_verify_location
    - slot{"location": null}
    - slot{"location_ok": false}
* restaurant_search{"location": "Pahalgam"}
    - slot{"location": "Pahalgam"}
    - action_verify_location
    - slot{"location": null}
    - slot{"location_ok": false}
* restaurant_search{"location": "Munnar"}
    - slot{"location": "Munnar"}
    - action_verify_location
    - slot{"location": null}
    - slot{"location_ok": false}
* restaurant_search{"location": "Alleppey"}
    - slot{"location": "Alleppey"}
    - action_verify_location
    - slot{"location": null}
    - slot{"location_ok": false}
* restaurant_search{"location": "Mysore"}
    - slot{"location": "Mysore"}
    - action_verify_location
    - slot{"location": "Mysore"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_budget
* restaurant_search{"budgetmin": "300", "budgetmax": "700"}
    - slot{"budgetmax": "700"}
    - slot{"budgetmin": "300"}
    - action_search_restaurants
    - slot{"location": "Mysore"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* send_mail{"send_email": "Yes please", "emailid": "suhail.momin05@gmail.com"}
    - slot{"emailid": "suhail.momin05@gmail.com"}
    - action_verify_email
    - slot{"emailid": "suhail.momin05@gmail.com"}
    - slot{"email_ok": true}
    - action_send_email
    - utter_ask_howcanhelp
* deny{"deny": "Finally"}
    - utter_goodbye
	- action_restarted

## interactive_story_27
* greet
    - utter_greet
* restaurant_search{"location": "Thane"}
    - slot{"location": "Thane"}
    - action_verify_location
    - slot{"location": null}
    - slot{"location_ok": false}
* restaurant_search{"location": "Chiplun"}
    - slot{"location": "Chiplun"}
    - action_verify_location
    - slot{"location": null}
    - slot{"location_ok": false}
* deny{"location": "Goa"}
    - slot{"location": "Goa"}
    - action_verify_location
    - slot{"location": "Goa"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budgetmin": "700", "budgetmax": "10000"}
    - slot{"budgetmax": "10000"}
    - slot{"budgetmin": "700"}
    - action_search_restaurants
    - slot{"location": "Goa"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* send_mail{"send_email": "do send", "emailid": "mtrworld@gmail.com"}
    - slot{"emailid": "mtrworld@gmail.com"}
    - action_verify_email
    - slot{"emailid": "mtrworld@gmail.com"}
    - slot{"email_ok": true}
    - action_send_email
    - utter_ask_howcanhelp
* deny{"deny": "Thats it"}
    - utter_goodbye
	- action_restarted

## interactive_story_28
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_location
* restaurant_search{"location": "Udupi"}
    - slot{"location": "Udupi"}
    - action_verify_location
    - slot{"location": null}
    - slot{"location_ok": false}
* restaurant_search{"location": "Rajkot"}
    - slot{"location": "Rajkot"}
    - action_verify_location
    - slot{"location": "Rajkot"}
    - slot{"location_ok": true}
    - utter_ask_budget
* restaurant_search{"budgetmin": "300", "budgetmax": "700"}
    - slot{"budgetmax": "700"}
    - slot{"budgetmin": "300"}
    - action_search_restaurants
    - slot{"location": "Rajkot"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* dont_send_email{"dont_send_email": "dont send"}
    - utter_ask_howcanhelp
* deny
    - utter_goodbye
	- action_restarted

## interactive_story_29
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Gangtok"}
    - slot{"location": "Gangtok"}
    - action_verify_location
    - slot{"location": null}
    - slot{"location_ok": false}
* restaurant_search{"location": "Shillong"}
    - slot{"location": "Shillong"}
    - action_verify_location
    - slot{"location": null}
    - slot{"location_ok": false}
* restaurant_search{"location": "Tripura"}
    - slot{"location": "Tripura"}
    - action_verify_location
    - slot{"location": null}
    - slot{"location_ok": false}
* restaurant_search{"location": "NOIDA"}
    - slot{"location": "NOIDA"}
    - action_verify_location
    - slot{"location": "NOIDA"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_budget
* restaurant_search{"budgetmin": "300", "budgetmax": "700"}
    - slot{"budgetmax": "700"}
    - slot{"budgetmin": "300"}
    - action_search_restaurants
    - slot{"location": "NOIDA"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* dont_send_email{"dot_send_email": "No"}
    - utter_ask_howcanhelp
* deny
    - utter_goodbye
	- action_restarted

## interactive_story_30
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_verify_location
    - slot{"location": "bangalore"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - utter_ask_budget
* restaurant_search{"budgetmin": "300", "budgetmax": "700"}
    - slot{"budgetmax": "700"}
    - slot{"budgetmin": "300"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* send_mail{"send_email": "Yes please", "emailid": "suhail.momin05@gmail.com"}
    - slot{"emailid": "suhail.momin05@gmail.com"}
    - action_verify_email
    - slot{"emailid": "suhail.momin05@gmail.com"}
    - slot{"email_ok": true}
    - action_send_email
    - utter_ask_howcanhelp
* deny{"deny": "No"}
    - utter_goodbye
	- action_restarted

## interactive_story_31
* greet
    - utter_greet
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_verify_location
    - slot{"location": null}
    - slot{"location_ok": false}
* restaurant_search{"location": "allahabad"}
    - slot{"location": "allahabad"}
    - action_verify_location
    - slot{"location": "allahabad"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budgetmax": "1000"}
    - slot{"budgetmax": "1000"}
    - action_search_restaurants
    - slot{"location": "allahabad"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* send_mail{"emailid": "suhail.momin05@gmail.com"}
    - slot{"emailid": "suhail.momin05@gmail.com"}
    - action_verify_email
    - slot{"emailid": "suhail.momin05@gmail.com"}
    - slot{"email_ok": true}
    - action_send_email
    - utter_ask_howcanhelp
* deny{"deny": "No"}
    - utter_goodbye
	- action_restarted

## interactive_story_32
* greet
    - utter_greet
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
    - action_verify_location
    - slot{"location": "Kolkata"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_budget
* restaurant_search{"budgetmax": "300"}
    - slot{"budgetmax": "300"}
    - action_search_restaurants
    - slot{"location": "Kolkata"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* affirm{"send_mail": "Yes please"}
    - utter_ask_emailid
* send_mail{"emailid": "adilhasan@gmail.com"}
    - slot{"emailid": "adilhasan@gmail.com"}
    - action_verify_email
    - slot{"emailid": "adilhasan@gmail.com"}
    - slot{"email_ok": true}
    - action_send_email
    - utter_ask_howcanhelp
* deny
    - utter_goodbye
	- action_restarted

## interactive_story_33
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - action_verify_location
    - slot{"location": "chandigarh"}
    - slot{"location_ok": true}
    - utter_ask_budget
* restaurant_search{"budgetmax": "300"}
    - slot{"budgetmax": "300"}
    - action_search_restaurants
    - slot{"location": "chandigarh"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* dont_send_email{"dont_send_email": "No thanks"}
    - utter_ask_howcanhelp
* deny{"deny": "No"}
    - utter_goodbye
	- action_restarted

## interactive_story_34
* greet
    - utter_greet
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
    - action_verify_location
    - slot{"location": "Kolkata"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_budget
* restaurant_search{"budgetmax": "300"}
    - slot{"budgetmax": "300"}
    - action_search_restaurants
    - slot{"location": "Kolkata"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* send_mail
    - utter_ask_emailid
* send_mail{"emailid": "adilhasan@gmail.com"}
    - slot{"emailid": "adilhasan@gmail.com"}
    - action_verify_email
    - slot{"emailid": "adilhasan@gmail.com"}
    - slot{"email_ok": true}
    - action_send_email
    - utter_ask_howcanhelp
* deny{"deny": "No"}
    - utter_goodbye
	- action_restarted

## interactive_story_35
* greet
    - utter_greet
* restaurant_search{"people": "100"}
    - utter_ask_location
* restaurant_search{"location": "bhubaneswar"}
    - slot{"location": "bhubaneswar"}
    - action_verify_location
    - slot{"location": "bhubaneswar"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_budget
* restaurant_search{"budgetmin": "1000", "budgetmax": "2000"}
    - slot{"budgetmax": "2000"}
    - slot{"budgetmin": "1000"}
    - action_search_restaurants
    - slot{"location": "bhubaneswar"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* dont_send_email
    - utter_ask_howcanhelp
* deny
    - utter_goodbye
	- action_restarted

## interactive_story_36
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "kakinada"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "kakinada"}
    - action_verify_location
    - slot{"location": "kakinada"}
    - slot{"location_ok": true}
    - utter_ask_budget
* restaurant_search{"budgetmin": "700"}
    - slot{"budgetmin": "700"}
    - action_search_restaurants
    - slot{"location": "kakinada"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* dont_send_email
    - utter_ask_howcanhelp
* deny
    - utter_goodbye
    - action_restarted

## interactive_story_37
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "kota"}
    - slot{"location": "kota"}
    - action_verify_location
    - slot{"location": null}
    - slot{"location_ok": false}
* restaurant_search{"location": "guntakal"}
    - slot{"location": "guntakal"}
    - action_verify_location
    - slot{"location": null}
    - slot{"location_ok": false}
* restaurant_search{"location": "Suryapet"}
    - slot{"location": "Suryapet"}
    - action_verify_location
    - slot{"location": null}
    - slot{"location_ok": false}
* restaurant_search{"location": "lko"}
    - slot{"location": "lko"}
    - action_verify_location
    - slot{"location": null}
    - slot{"location_ok": false}
* restaurant_search{"location": "surat"}
    - slot{"location": "surat"}
    - action_verify_location
    - slot{"location": "surat"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_budget
* restaurant_search{"budgetmax": "700"}
    - slot{"budgetmax": "700"}
    - action_search_restaurants
    - slot{"location": "surat"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* dont_send_email
    - utter_ask_howcanhelp
* goodbye
    - utter_goodbye
    - action_restarted

## interactive_story_38
* greet
    - utter_greet
* restaurant_search{"location": "chapra"}
    - slot{"location": "chapra"}
    - action_verify_location
    - slot{"location": null}
    - slot{"location_ok": false}
* restaurant_search{"location": "secundarabad"}
    - slot{"location": "secundarabad"}
    - action_verify_location
    - slot{"location": null}
    - slot{"location_ok": false}
* restaurant_search{"location": "kharagpur"}
    - slot{"location": "kharagpur"}
    - action_verify_location
    - slot{"location": null}
    - slot{"location_ok": false}
* restaurant_search{"location": "secunderabad"}
    - slot{"location": "secunderabad"}
    - action_verify_location
    - slot{"location": null}
    - slot{"location_ok": false}
* restaurant_search{"location": "hyderabad"}
    - slot{"location": "hyderabad"}
    - action_verify_location
    - slot{"location": "hyderabad"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_budget
* restaurant_search{"budgetmin": "100", "budgetmax": "500"}
    - slot{"budgetmax": "500"}
    - slot{"budgetmin": "100"}
    - action_search_restaurants
    - slot{"location": "hyderabad"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* send_mail{"emailid": "mudassar.iiita@gmail.c"}
    - slot{"emailid": "mudassar.iiita@gmail.c"}
    - action_verify_email
    - slot{"emailid": null}
    - slot{"email_ok": false}
* send_mail{"emailid": "mudassar.iiita@gmail.com"}
    - slot{"emailid": "mudassar.iiita@gmail.com"}
    - action_verify_email
    - slot{"emailid": "mudassar.iiita@gmail.com"}
    - slot{"email_ok": true}
    - action_send_email
    - utter_ask_howcanhelp
* goodbye
    - utter_goodbye
    - action_restarted

## interactive_story_39
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_verify_location
    - slot{"location": "bangalore"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - utter_ask_budget
* restaurant_search{"budgetmin": "300", "budgetmax": "700"}
    - slot{"budgetmax": "700"}
    - slot{"budgetmin": "300"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* send_mail{"emailid": "suhail.momin05@gmail.com"}
    - slot{"emailid": "suhail.momin05@gmail.com"}
    - action_verify_email
    - slot{"emailid": "suhail.momin05@gmail.com"}
    - slot{"email_ok": true}
    - action_send_email
    - utter_ask_howcanhelp
* deny
    - utter_goodbye
    - action_restarted

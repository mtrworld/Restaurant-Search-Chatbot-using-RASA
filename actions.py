from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

#Import the all the important libraries
from rasa_sdk import Action
from rasa_sdk.events import SlotSet
from rasa_sdk.events import Restarted
import zomatopy
import json
import requests
import asyncio
import re
#For parsing the webpages
from bs4 import BeautifulSoup
import urllib3
urllib3.disable_warnings()
#For sending email
import smtplib
from concurrent.futures import ThreadPoolExecutor
r_email_rest = []
from email.message import EmailMessage

#This class searches for the restaurants and displays them in descendinng order of Average User Rating
class ActionSearchRestaurants(Action):
    #Define action
    def name(self):
        return 'action_search_restaurants'

    def run(self, dispatcher, tracker, domain):
        #Key to connect to Zomato API
        config={ "user_key":"******"}
        zomato = zomatopy.initialize_app(config)
        loc = tracker.get_slot('location')

        #Get all slots information
        cuisine = tracker.get_slot('cuisine')
        cost_min = tracker.get_slot('budgetmin')
        cost_max = tracker.get_slot('budgetmax')
        
        #If only minimum cost in specified
        if (cost_min and cost_max== None):
            cost_max = '10000'
        if (cost_min == None and cost_max):
            cost_min='0'
        print(cost_min)
        print(cost_max)
        
        results, lat, lon = self.get_location_suggestions(loc,zomato)

        if (results == 0):
            # Zomato API could not find suggestions for this location.
            restaurant_exist = False
            dispatcher.utter_message("Sorry, no results found in this location:("+ "\n")
        else:
            r_rest = self.get_restaurants(lat, lon, cost_min, cost_max, cuisine)

            # Filter the results based on budget
            r_budget = [r_rest_single for r_rest_single in r_rest if ((r_rest_single['restaurant']['average_cost_for_two'])> int(cost_min)) & (
                r_rest_single['restaurant']['average_cost_for_two'] < int(cost_max))]
            # Sort the results according to the restaurant's rating
            r_budget_rating_sorted = sorted(
                r_budget, key=lambda k: float(k['restaurant']['user_rating']['aggregate_rating']), reverse=True)

            # Build the response for displaying restaurant information
            response = ""
            restaurant_exist = False
            if len(r_budget_rating_sorted) == 0:
                dispatcher.utter_message("Sorry, no results found :("+ "\n")
            else:
                # Pick the top 5
                r_budget_rating_top5 = r_budget_rating_sorted[:5]
                global r_email_rest
                r_email_rest = r_budget_rating_sorted[:10]
                if(r_email_rest and len(r_email_rest) > 0):
                    restaurant_exist = True
                rest_num = 0
                for restaurant in r_budget_rating_top5:
                    rest_num +=1
                    response = response + "Restaurant " + str(rest_num) + ": " + str(restaurant['restaurant']['name']) + " in " + str(restaurant['restaurant']['location']['address']) + " has been rated " + str(restaurant['restaurant']['user_rating']['aggregate_rating']) + "\n" + "\n" + "\n" 
                dispatcher.utter_message("Here are our picks!"+ "\n" + response)
        return [SlotSet('location', loc), SlotSet('restaurant_exist', restaurant_exist)]

    #Get location suggestions
    def get_location_suggestions(self, loc, zomato):
        # Get location details including latitude and longitude
        location_detail = zomato.get_location(loc, 1)
        d1 = json.loads(location_detail)
        lat = 0
        lon = 0
        results = len(d1["location_suggestions"])
        if (results > 0):
            lat = d1["location_suggestions"][0]["latitude"]
            lon = d1["location_suggestions"][0]["longitude"]
        return results, lat, lon
    
    #Get Restaurants Suggestions
    def get_restaurants(self, lat, lon, budgetmin, budgetmax , cuisine):
        #Define cuisine dictionary with related codes
        cuisines_dict = {'american': 1, 'chinese': 25, 'italian': 55,
                         'mexican': 73, 'north indian': 50, 'south indian': 85}
        r_rest = []
        executor = ThreadPoolExecutor(max_workers=5)
        #Extract restaurants
        for res_key in range(0, 101, 20):
            executor.submit(retrieve_restaurant, lat, lon, cuisines_dict, cuisine, res_key, r_rest)
        executor.shutdown()
        return r_rest

#This class verifies location enterted by the user
#If its servicable location by Zomato as in Tier 1 and 2. Move on with restaurant Search
#If its valid city in India and not servicable by Zomato display appropriate message
#If its invalid city return error and ask for city name again
class VerifyLocation(Action):
    #Define action
    def name(self):
        return "action_verify_location"
    
    def run(self, dispatcher, tracker, domain): 
        #Extract the list of tier 1 and 2 cities from wikipage
        url="https://en.wikipedia.org/wiki/Classification_of_Indian_cities"
        r = requests.get(url,verify=False)
        soup = BeautifulSoup(r.text, "html.parser")
    
        #Parse the content to extract names
        cities=list(map(lambda x:x.text.lower(),soup.find('table',class_='wikitable').find_all('a')))
        
        #Get the list of common synonym names for the cities in tier 1 and 2
        city_synonym=[]
        #Extract the common city synonyms from this page
        r=requests.get('https://www.scoopwhoop.com/news/whats-in-a-name/#.45rdcz1m2',verify=False)
        synonym_list=BeautifulSoup(r.text,'html.parser').find('div',class_='article-body').find_all('h2')
        
        #extract Synonym list
        for city in synonym_list:
            if re.search(r'^[0-9]{1,2}.+',city.text.strip()):
                city_synonym.append(city.text.strip().split()[1].lower())
                city_synonym.append(city.text.strip().split()[-1].lower())        
        
        #Few other city synonyms as gathered from the internet
        city_synonym_2 = ['allahabad','atal-nagar','bangalore','baroda','bejawada ','belagavi ','belgaum','benares','bengaluru',
                        'bijapur','bombay','calcutta ','calicut','cannanore','cawnpore ','chennai','cochin','gauhati',
                        'gulbarga ','gurgaon','gurugram ','guwahati ','hubballi ','hubli ','indhur','indore','jabalpur ',
                        'jajesmow ','jajmau','jubbulpore ','kalaburagi ','kannur','kanpur','kochi ','kolkata','kollam',
                        'kozhikode','kudanthai','kumbakonam ','madras','mangalore','mangaluru','mumbai','bombay','mysore','mysore',
                        'mysuru','nellore','panaji','panjim','pondicherry','poona ','prayagraj','puducherry ','pune',
                        'quilon','raipur','shimla','simhapuri','simla ','thiruvananthapuram','thrissur ','tindivanam ',
                        'tinnevelly ','tinthirivanam ','tiruchirapalli','tirunelveli','tiruvallikeni ','trichinopoly',
                        'trichur','triplicane ','trivandrum ','vadodara ','varanasi ','vatakara ','vijayapura ','vijayawada ',
                        'visakhapatnam ','waltair']
        
        #List of all valid cities in India for verification. Parse from this page
        url1="https://en.wikipedia.org/wiki/List_of_cities_in_India_by_population"
        r1 = requests.get(url1,verify=False)
        soup1 = BeautifulSoup(r1.text, "html.parser")
        
        #Extract list of all cities in India
        all_cities_list = []
        temp_city=list(map(lambda x:x.text.lower(),soup1.find('table',class_='wikitable').find_all('a')))
        for city in temp_city:
            if not re.search(r'^.[0-9]{1,2}.+',city):
                all_cities_list.append(city)

        #get the location from user slot
        loc=tracker.get_slot('location')
        
        #Check for pincodes. Not supported for now
        if (loc.lower().isdigit()):
            dispatcher.utter_message("Sorry I am naive I dont understand pincodes and digits for now. Please try some actual place!!")
            return [SlotSet('location', None), SlotSet("location_ok", False)]
        #Check for invalid city
        elif not (loc.lower() in all_cities_list  or loc.lower() in city_synonym or loc.lower() in city_synonym_2 or loc.lower() in cities):
            dispatcher.utter_message("Sorry did'nt find any such location " + loc + " Can you please tell again?")
            return [SlotSet('location', None), SlotSet("location_ok", False)]
        #Check for valid city but no servicable by Zomato
        elif not (loc.lower() in city_synonym or loc.lower() in city_synonym_2 or loc.lower() in cities):
            dispatcher.utter_message("We do not operate in " + loc + " yet. Please try some other city.")
            return [SlotSet('location', None), SlotSet("location_ok", False)]
        #If valid city and servicable return true
        else:
            return [SlotSet('location',loc),SlotSet('location_ok',True)]

#This class sends email to user entered email List
class ActionSendEmail(Action):
    #Define action name
    def name(self):
        return 'action_send_email'
        

    def run(self, dispatcher, tracker, domain):
        #Get user's email id
        to_email = tracker.get_slot('emailid')

        #Get location and cuisines to put in the email
        loc = tracker.get_slot('location')
        cuisine = tracker.get_slot('cuisine')
        global r_email_rest
        email_rest_count = len(r_email_rest)
        #Construct the email 'subject' and the contents.
        r_email_subj = "Top " + str(email_rest_count) + " " + cuisine.capitalize() + " restaurants in " + str(loc).capitalize()
        r_email_msg = "Hello this is your personal Foodie assistant. As per your requirements, here are the " + r_email_subj + "." + "\n" + "\n" +"\n"
        rest_num = 0
        for restaurant in r_email_rest:
            rest_num +=1
            r_email_msg = r_email_msg + "Restaurant " + str(rest_num) +": " + str(restaurant['restaurant']['name'])+ " in " + str(restaurant['restaurant']['location']['address']) + " has been rated " + str(restaurant['restaurant']['user_rating']['aggregate_rating']) + ".The average budget for 2 people is: " + str(restaurant['restaurant']['average_cost_for_two']) + "\n" + "\n"

        #Open SMTP connection to Foodie's email id.
        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()
        s.login("******@gmail.com", "**********")

        #Create the msg object
        msg = EmailMessage()

        #Fill in the message properties
        msg['Subject'] = r_email_subj
        msg['From'] = "mfoodiechat@gmail.com"

        #Fill in the message content
        msg.set_content(r_email_msg)
        msg['To'] = to_email
        
        #Sent the message. If error catch and throw it
        try:
            s.send_message(msg)
            s.quit()
            dispatcher.utter_message("Email Sent. Please check your inbox. Have a great time!!")
        except (RuntimeError, TypeError, NameError, AttributeError):
            dispatcher.utter_message("Email server not responding at time")
        return []

#global function to retrieve restaurants from Zomato
def retrieve_restaurant(lat, lon, cuisines_dict, cuisine, res_key, r_rest):
    base_url = "https://developers.zomato.com/api/v2.1/"
    headers = {'Accept': 'application/json',
                'user-key': '**********'}
    try:
        results = (requests.get(base_url + "search?" + "&lat=" + str(lat) + "&lon=" + str(lon) + "&cuisines=" + str(
            cuisines_dict.get(cuisine)) + "&start=" + str(res_key)+"&count=20", headers=headers).content).decode("utf-8")
    except:
        return
    d = json.loads(results)
    r_rest.extend(d['restaurants'])
    
#This class checks for email validity
#The email entered must be valid before send email. This one check it.
class EmailVerificationLocation(Action):
    #define action name
    def name(self):
        return "action_verify_email"
    
    def run(self, dispatcher, tracker, domain):
        email_id = tracker.get_slot('emailid')
        print(email_id)
        #Check the email pattern
        regex_email = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
        
        #If valid return email if else error message
        if (re.search(regex_email,email_id)):
            return [SlotSet('emailid', email_id),SlotSet('email_ok',True)]
        else:
            dispatcher.utter_message("Seems you have entered a wrong email id. Please check and enter again!!!")
            return [SlotSet('emailid', None),SlotSet('email_ok',False)]
            
        
#Reset all the values at the end of the story        
class ActionRestarted(Action):
    def name(self):
        return 'action_restarted'
        
    def run(self, dispatcher, tracker, domain):
        return[Restarted()]         

#!/usr/bin/python

import urllib2

import json

import datetime

import re

import subprocess 

import sqlite3

import sys 

from twilio.rest import TwilioRestClient

# Twilio Account Info
account_sid = "" # Get sid from twilio

auth_token = "" # get auth_token from twilio

client = TwilioRestClient(account_sid,auth_token)

# Create sqlite connection

conn = sqlite3.connect('messages.db')

curs = conn.cursor()

from datetime import date,timedelta

# Calling url to get the json response.
response = urllib2.urlopen("http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/significant_hour.geojson")

jsonResponse = json.load(response)

for index in range(len(jsonResponse["features"])):

    location = jsonResponse["features"][index]["properties"]["place"]

    magnitude = jsonResponse["features"][index]["properties"]["mag"]
    
    time = jsonResponse["features"][index]["properties"]["time"]

    readableTime = datetime.datetime.fromtimestamp(float(time)/1000.).strftime('%Y-%m-%d %H:%M:%S')

    sentMessage = 'Yes'

    if "Nepal" in location:
        message = "Recent Earthquake of M " + str(magnitude) + " strikes off " + location + " at " + readableTime + "."

	curs.execute('CREATE TABLE IF NOT EXISTS message(datestamp TEXT, message TEXT not null unique, sentMessage TEXT)')

	try:	
	    curs.execute('INSERT INTO message (datestamp, message, sentMessage) VALUES(?,?,?)', (readableTime, message, sentMessage))
	    
	    subprocess.check_call(['/home/pi/pushbullet.sh', str(message)])
		
	    phoneNumbers= ['phoneNumber1','phoneNumber2','phoneNumber3']
		
            for i in range(len(phoneNumbers)):
                client.messages.create(body=message, to=phoneNumbers[i], from_="your_twilio_number_here")	
	    
	except sqlite3.IntegrityError as e:
	    print ('sqlite error: ', e.args[0]) # Column value is not unique
	   
	    sys.exit() # No need to continue

conn.commit()
curs.close()
conn.close()

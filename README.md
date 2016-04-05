# Earthquake-Notifier
Python script to send notifications to a list of phone numbers if usgs reports a significant earthquake in Nepal.

Project Objective:
1. To send and receive noifications when a significant earthquake hits Nepal.
2. Needs to run near real time so had to use raspberry pi to conserve resources. Due to raspberry model complications, I had to update the code to not write to only write to the db when there is unique data. 
3. Since USGS apis are updated every 5 minutes, this python script will run every 5 minutes on the cron. 

Project Hardware:
1. Raspberry Pi first generation (512MB RAM)

Used:
1. Sqlite3 db.
2. Python
3. Twilio (for sms notification)
4. Pushbullet Api (for in App notification)


Any updates and comments are welcome. Thank you. 

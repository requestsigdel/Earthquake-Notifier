# Earthquake-Notifier
Python script to send notifications to a list of phone numbers if usgs reports a significant earthquake in Nepal.

<b>Project Objective:</b><br />
1. To send and receive noifications when a significant earthquake hits Nepal.<br />
2. Needs to run near real time so had to use raspberry pi to conserve resources. Due to raspberry model complications, I had to update the code to not write to only write to the db when there is unique data. <br />
3. Since USGS apis are updated every 5 minutes, this python script will run every 5 minutes on the cron. <br />

<b>Project Hardware:</b><br />
1. Raspberry Pi first generation (512MB RAM)

<b>Used:</b><br />
1. Sqlite3 db. <br />
2. Python <br />
3. Twilio (for sms notification) <br />
4. Pushbullet Api (for in App notification) <br />


Any updates and comments are welcome. Thank you. 

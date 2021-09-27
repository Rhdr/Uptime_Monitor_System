# Uptime_Monitor_System
A website up/down monitoring system. 

# Features:
- Real-time monitoring of websites up/down statuses
- Dynamically add, edit & delete websites to be monitored 
- Register a slack api app token & channel to receive real time status updates to slack 

# Slack Setup:
- On the slack api website, create a slack app/bot with chat-write permissions, install it and generate a OAuth token
- Next on the main slack website, add the new slack app/bot to your channel 
- Lastly when using this app and adding/editing a website, insert your slack token & slack channel.
Slack is now linked and you will now receive status changes for as long as this app runs

# How to start the localhost Django Server:
- Download the repo and open in terminal.
- CD one level down to the Uptime_Monitor_System folder (cd downloaded_repo_location/Uptime_Monitor_System)
- Run the following command to start a localhost server: python manage.py runserver
- Open your browser and go to http://127.0.0.1:8000/ to view the website

# Tech used:
- Django
- JQuery & Ajax(GET & POSTS)
- Bootstrap
- SQLLite

# Dependencies:
- Django==3.2.5
- requests==2.26.0
- python-dotenv==0.19.0
- slackclient==2.9.3

# Django Super user
- Username: Rheeder
- Password: 12345Sinov8
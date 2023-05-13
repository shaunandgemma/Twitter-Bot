Twitter Automation Using Tweepy
This is a Python script that uses the Tweepy library to automate various Twitter actions, such as fetching home timeline tweets, getting user data, following/unfollowing followers, and liking tweets.

Requirements
In order to use this script, you will need to have a Twitter account and create a Twitter developer account to obtain the following:

Twitter API Key
Twitter API Secret Key
Twitter Access Token
Twitter Access Token Secret
Once you have obtained these credentials, you need to put them in the config.py file in the following format:

makefile
Copy code
API_KEY = "your_api_key_here"
API_SECRET = "your_api_secret_here"
ACCESS_TOKEN = "your_access_token_here"
ACCESS_SECRET = "your_access_token_secret_here"
Usage
Clone this repository to your local machine
Install the Tweepy library by running pip install tweepy in your terminal
Replace the credentials in the config.py file with your own credentials
Open the main.py file in your code editor and run the script to perform the desired Twitter actions.
Home Timeline Tweets
To get tweets from your home timeline, uncomment the code in lines 7-9 of main.py file.

User Data
To get user data, such as location, profile bio, name, Twitter handle, number of followers and following, uncomment the code in lines 13-20 of main.py file.

Follow/Unfollow Your Followers
To follow or unfollow your followers, uncomment the code in lines 24-35 of main.py file. Change the name of the user you want to follow in line 28.

Like a Random Tweet Assigned to String
To like a tweet, uncomment the code in lines 38-45 of main.py file. Change the value of the search variable to the keyword you want to search for, and change the numberOfTweets variable to the number of tweets you want to like.

Disclaimer
This script is for educational purposes only. Please use it responsibly and do not abuse Twitter's terms of service.

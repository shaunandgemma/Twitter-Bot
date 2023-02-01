import tweepy
import config

# auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)
# api = tweepy.API(auth)

##################################Twitter Home Timeline Tweets##################################

consumer_key = config.API_KEY
consumer_secret = config.API_SECRET
access_token = config.ACCESS_TOKEN
access_token_secret = config.ACCESS_SECRET

auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text) # prints home timeline

# ##################################Twitter Home Timeline Tweets##################################

# ##################################Data From User##################################

user = api.get_user(screen_name='ShaunandGemma') # Get the users name you want the data for
# # print(user) # Gives all the extensions you can use to obtain information
print(user.location) # prints users location
print(user.description) # prints profile bio
print(user.name)  # prints your full name.
print(user.screen_name) # prints your Twitter name.
print(user.followers_count) # Prints how many followers you have
print(user.friends_count) # prints how many the user is following
for friend in user.friends():
    print(friend.screen_name)

#################################Follow/Unfollow Your Followers###########################

import time

def limit_handler(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.TooManyRequests:
            time.sleep(1000)
        except StopIteration:
            break

for follower in limit_handler(tweepy.Cursor(api.get_followers).items()):
    if follower.name == 'Gemma': # if the specified user follows user
        print(follower.name)                  # prints names of who follows the user
        follower.follow()                     # follows the specified user back
      # follower.unfollow()                   # unfollows the specified user

#################################Like a Random Tweet Assigned to String###########################

search = "Elon Musk"
numberOfTweets = 30

# Be a narcisist and love your own tweets. or retweet anything with a keyword!
for tweet in tweepy.Cursor(api.search_tweets, search).items(numberOfTweets):
    try:
        tweet.favorite()
        print('Like this tweet')
    except tweepy.TweepyException as e:
        print(e)
    except StopIteration:
        break





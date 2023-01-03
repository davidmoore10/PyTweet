import tweepy


# Open the file
with open('tokens.txt', 'r') as file:
    # Read the lines of the file into a list
    lines = file.readlines()

secrets = []
# Iterate over the lines of the file
for line in lines:
    secrets.append(line.strip())
print(secrets)

# API Keys and Secret Keys
consumer_key = 'yGavonYU6a33nanCZxr2ZVSkH'
consumer_secret = secrets[0]
access_token = '1610319530856775683-okk66eJrhYM37hfIfX2ewN889IX3EP'
access_token_secret = secrets[1]

# Authenticate with Twitter API
auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Tweet to your account
tweet = input()
api.update_status(tweet)
import os
import tweepy

# Your Twitter API credentials
consumer_key = '2WqKFA9eNwnyoCz7Q0lmXkqHO'
consumer_secret = 'SGQNhTr2oO0f6HrMhHYCbQrAhrzxIbDW3D6QNdM2aKtggFZJfZ'
access_token = 'AAAAAAAAAAAAAAAAAAAAAN%2BlwAEAAAAAzuecaLTKcXuxKuD%2FmnuA4nfzQI8%3D5jCaTn4ZPdRqPlg6LemQqxDJl7EFITX2Ka3wAz7zlI0Jih5dvC'
access_token_secret = 'Z3TixzpsNXmgcdCYXiTGsu6Qf3D2cGdMCbih1BjWZaGOS'

# Authenticate with the Twitter API
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Check if authentication was successful
try:
    api.verify_credentials()
    print("Authentication OK")
except Exception as e:
    print(f"Error during authentication: {e}")

# Scrape tweets from a user
users = ['elzoukinadir1', 'nadirelzouki']  # Ensure usernames are correct
for user in users:
    print(f'Tweets by {user}:')
    try:
        tweets = api.user_timeline(screen_name=user, count=5)
        for tweet in tweets:
            print(f'{tweet.created_at} - {tweet.text}')
    except Exception as e:
        print(f"Error fetching tweets for {user}: {e}")

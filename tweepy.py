import tweepy

#consumer_key = 'YOUR_CONSUMER_KEY'
#consumer_secret = 'YOUR_CONSUMER_SECRET'
client_id = 'Nm0xbWk4M3ExcnNjWUE4QVpvMFo6MTpjaQ'
client_secret = 'mIy4Mmm-uIjqNEegrfbsxiije3jIfueAFcpfpPOCga2ylZYlAc'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAAuTuQEAAAAA5QQ7IhFZ0YBel5frCzG9OOzT%2FuE%3DVH0WRGOgusldlL509McRywmDFMdtTDbTgKR9MadGgGIINCBW3v'
client = tweepy.Client(bearer_token=bearer_token)
tweet_text = "Hello, Twitter! #MyFirstTweet"
response = client.create_tweet(text=tweet_text)
print("Tweet posted:", response.data)
print(10//3)
#curl "https://api.twitter.com/2/users/by/username/angel_chukss" -H "Authorization: Bearer AAAAAAAAAAAAAAAAAAAAAAuTuQEAAAAA5QQ7IhFZ0YBel5frCzG9OOzT%2FuE%3DVH0WRGOgusldlL509McRywmDFMdtTDbTgKR9MadGgGIINCBW3v"
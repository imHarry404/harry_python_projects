import tweepy
from time import sleep


auth=tweepy.OAuthHandler('your-api-key','your-api-secret-key')

auth.set_access_token('access-token-key','access-token-secret')


# authorizing the api's
api=tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

search_keywords ='python'
nrTweets=100

for tweet in tweepy.Cursor(api.search,search_keywords).items(nrTweets):
    try:
        tweet.favorite()
        print('tweet liked')
        tweet.retweet()
        print('tweet retweeted')
        sleep(300) #sleep for 5 minutes
    except tweepy.TweepError as e:
        pass
    except StopIteration:
        break

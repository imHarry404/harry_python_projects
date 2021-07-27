import tweepy
from time import sleep


auth=tweepy.OAuthHandler('pURfxcPsgnmy5JKFiZrLL73sA','ORNkx1hRZqwZypQxnTqOvXtuBBAbautf1wJF5ZO5kyF8ySa62w')

auth.set_access_token('1029273003442483201-YIBWSZ4zg19UHtFw7N1QIv7MNwBo7U','fDbOszxyEbuowdND368LFdzd8aNlVEuPN5WVZTIB1CFCu')

# authorizing the api's
api=tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

search_keywords ='machine learning'
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

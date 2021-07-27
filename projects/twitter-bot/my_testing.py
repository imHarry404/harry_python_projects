import tweepy
import time

auth=tweepy.OAuthHandler('pURfxcPsgnmy5JKFiZrLL73sA','ORNkx1hRZqwZypQxnTqOvXtuBBAbautf1wJF5ZO5kyF8ySa62w')

auth.set_access_token('1029273003442483201-YIBWSZ4zg19UHtFw7N1QIv7MNwBo7U','fDbOszxyEbuowdND368LFdzd8aNlVEuPN5WVZTIB1CFCu')

api=tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
user=api.me()


# print(user)
# print(user.screen_name) #this will tell your name
# print(user.followers_count) #this will tell your followers count



'''

# to print the name of all your followers

for followers in tweepy.Cursor(api.followers).items():
    print(followers.name) #it it hit the rate limit , it will pause automatically for a while then it will resume automatically
'''

'''
# to follow back a particular followers we can do this

for followers in tweepy.Cursor(api.followers).items():
    if followers.name=='follower_name':
        followers.follow()
'''


# to like a tweet by searching for a particular keyword
search_keywords ='javascript'
nrTweets=500 #means how many tweets you want to like, 24 hr limit is 1k

for tweet in tweepy.Cursor(api.search,search_keywords).items(nrTweets):
    try:
        print('tweet liked')
        tweet.favorite() #to like
        tweet.retweet() #to retweet
        time.sleep(5) #waiting for 5 seconds for next tweet to like otherwise it will very fast and twitter will ban us
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

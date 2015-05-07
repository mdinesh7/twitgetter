import tweepy
from config import consumer_key, consumer_secret, access_token, \
    access_token_secret

# Authenticate
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


def search_twit(term):
    '''Get data'''
    if term:
        tweet = api.search(term)
        print tweet
    else:
        print 'Please pass search query to search_twit'

if __name__ == '__main__':
    search_twit('search term here.')



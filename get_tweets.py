from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

from config import consumer_key, consumer_secret, access_token, \
    access_token_secret, search_terms

# Authenticate
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


class SearchTwit(StreamListener):

    def on_data(self, data):
        '''If data exists'''
        twit = data
        print dir(twit)
        return True

    def on_error(self, status):
        '''If there is any error'''
        print status


if __name__ == '__main__':
    twit_obj = SearchTwit()
    twit_stream = Stream(auth, twit_obj)

    if isinstance(search_terms, list):
        if len(search_terms) == 0:
            print 'Empty list'
        elif len(search_terms) > 0:
            twit_stream.filter(track=search_terms)
    else:
        'input should be list'

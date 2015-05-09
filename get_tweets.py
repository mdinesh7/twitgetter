import tweepy

from config import consumer_key, consumer_secret, access_token, \
    access_token_secret, search_terms

# Authenticate
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


class SearchTwit(terms):

    def on_data(self, data):
        '''If data exists'''
        print data
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
            stream.filter(track=search_terms)
    else:
        'input should be list'

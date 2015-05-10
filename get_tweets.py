from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from pymongo import MongoClient

import json

from config import consumer_key, consumer_secret, access_token, \
    access_token_secret, search_terms, db_name, col_name

# Authenticate
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


# Mongodb Connection
client = MongoClient('localhost', 27017)
db = client.db_name

collection = db.col_name


class SearchTwit(StreamListener):

    def on_data(self, data):
        '''If data exists'''
        # All twit data
        twit = json.loads(data)

        # twit location
        if twit.get('geo'):
            geo_type = twit['geo']['type']
            latitude = twit['geo']['coordinates'][0]
            longitude = twit['geo']['coordinates'][1]
        elif twit.get('coordinates'):
            geo_type = twit['coordinates']['type']
            latitude = twit['geo']['coordinates'][1]
            longitude = twit['geo']['coordinates'][0]
        else:
            geo_type = ''
            latitude = ''
            longitude = ''

        # Twit place details
        if twit.get('place'):
            place_type = twit['place']['place_type']
            place_name = twit['place']['place_name']
            place_full_name = twit['place']['place_full_name']
            place_country_code = twit['place']['place_country_code']
            place_country = twit['place']['place_country']

            if twit.get('place').get('bounding_box'):
                place_bounding_box_type = twit['place']['bounding_box']['type']
                place_bounding_box_coordinates = twit[
                    'place']['bounding_box']['coordinates'][0]
        else:
            place_type = ''
            place_name = ''
            place_full_name = ''
            place_country_code = ''
            place_country = ''
            place_bounding_box_type = ''
            place_bounding_box_coordinates = ''

        collection.insert({
            'created_at': twit['created_at'],
            'text': twit['text'],
            'source': twit['source'],
            'retweet_count': twit['retweet_count'],
            'favorite_count': twit['favorite_count'],
            'timestamp': twit['timestamp_ms'],

            # User
            'user_id': twit['user']['id'],
            'user_name': twit['user']['name'],
            'user_screen_name': twit['user']['screen_name'],
            'user_location': twit['user']['location'],
            'user_verified': twit['user']['verified'],
            'user_followers_count': twit['user']['followers_count'],
            'user_friends_count': twit['user']['friends_count'],
            'user_listed_count': twit['user']['listed_count'],
            'user_favourites_count': twit['user']['favourites_count'],
            'user_statuses_count': twit['user']['statuses_count'],
            'user_account_created_at_date': twit['user']['created_at'],
            'user_utc_offset': twit['user']['utc_offset'],
            'user_time_zone': twit['user']['time_zone'],
            'user_geo_enabled': twit['user']['geo_enabled'],
            'user_lang': twit['user']['lang'],

            'geo_type': geo_type,
            'latitude': latitude,
            'longitude': longitude,
            'place_type': place_type,
            'place_name': place_name,
            'place_full_name': place_full_name,
            'place_country_code': place_country_code,
            'place_country': place_country,
            'place_bounding_box_type': place_bounding_box_type,
            'place_bounding_box_coordinates': place_bounding_box_coordinates
        })
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

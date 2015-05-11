from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import json
from time import gmtime, strftime

from config import consumer_key, consumer_secret, access_token, \
    access_token_secret, search_terms, collection

# Authenticate
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


class SearchTwit(StreamListener):

    def on_data(self, data):
        '''If data exists'''
        # All twit data
        twit = json.loads(data)

        # twit location
        if twit.get('geo'):
            geo_type = twit.get('geo').get('type')
            coordinates = twit.get('geo').get('coordinates')
            if coordinates:
                latitude = coordinates[0]
                longitude = coordinates[1]
        elif twit.get('coordinates'):
            geo_type = twit.get('coordinates').get('type')
            coordinates = twit.get('geo').get('coordinates')
            if coordinates:
                latitude = coordinates[1]
                longitude = coordinates[0]
        else:
            geo_type = ''
            latitude = ''
            longitude = ''

        # Twit place details
        if twit.get('place'):
            place_type = twit.get('place').get('place_type')
            place_name = twit.get('place').get('place_name')
            place_full_name = twit.get('place').get('place_full_name')
            place_country_code = twit.get('place').get('place_country_code')
            place_country = twit.get('place').get('place_country')

            if twit.get('place').get('bounding_box'):
                place_bounding_box_type = twit.get('place').get('bounding_box').get('type')
                place_bounding_box_coordinates_value = twit.get(
                    'place').get('bounding_box').get('coordinates')
                if place_bounding_box_coordinates:
                    place_bounding_box_coordinates_value[0]
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
            'place_bounding_box_coordinates': place_bounding_box_coordinates,
            'twit_written_to_db': strftime("%Y-%m-%d %H:%M:%S", gmtime())
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

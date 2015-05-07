import tweepy

from config import consumer_key, consumer_secret, access_token, \
    access_token_secret, search_terms

# Authenticate
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


def search_twit(terms):
    '''Get data from firehose'''
    if len(terms) == 0:
        print 'No search terms in the list'
    if len(terms) == 1:
        # return 100 results- which is max limit per page.
        tweets = api.search(
            terms[0], rpp=100, headers={'User-Agent': 'tweepy'})
        for tweet in tweets:
            truncated = tweet.truncated
            text = tweet.text
            created_at = tweet.created_at
            in_reply_to_status_id = tweet.in_reply_to_status_id
            the_id = tweet.id  # Instead of id, I am using the_id
            favorite_count = tweet.favorite_count

            # User
            user_follow_request_sent = tweet.author.follow_request_sent
            user_profile_use_background_image = tweet.author.profile_use_background_image
            user_follow_request_sent = tweet.author._json[
                'follow_request_sent']
            user_profile_use_background_image = tweet.author._json[
                'profile_use_background_image']
            user_default_profile_image = tweet.author._json[
                'default_profile_image']
            user_id = tweet.author._json['id']
            user_profile_background_image_url_https = tweet.author._json[
                'profile_background_image_url_https']
            user_verified = tweet.author._json['verified']
            user_profile_text_color = tweet.author._json['profile_text_color']
            user_profile_image_url_https = tweet.author._json[
                'profile_image_url_https']
            user_profile_sidebar_fill_color = tweet.author._json[
                'profile_sidebar_fill_color']
            user_followers_count = tweet.author._json['followers_count']
            user_profile_sidebar_border_color = tweet.author._json[
                'profile_sidebar_border_color']
            user_id_str = tweet.author._json['id_str']
            user_profile_background_color = tweet.author._json[
                'profile_background_color']
            user_listed_count = tweet.author._json['listed_count']
            user_is_translation_enabled = tweet.author._json[
                'is_translation_enabled']
            user_utc_offset = tweet.author._json['utc_offset']
            user_statuses_count = tweet.author._json['statuses_count']
            user_description = tweet.author._json['description']
            user_friends_count = tweet.author._json['friends_count']
            user_location = tweet.author._json['location']
            user_profile_link_color = tweet.author._json['profile_link_color']
            user_profile_image_url = tweet.author._json['profile_image_url']
            user_following = tweet.author._json['following']
            user_geo_enabled = tweet.author._json['geo_enabled']
            user_profile_background_image_url = tweet.author._json[
                'profile_background_image_url']
            user_screen_name = tweet.author._json['screen_name']
            user_lang = tweet.author._json['lang']
            user_profile_background_tile = tweet.author._json[
                'profile_background_tile']
            user_favourites_count = tweet.author._json['favourites_count']
            user_name = tweet.author._json['name']
            user_notifications = tweet.author._json['notifications']
            user_url = tweet.author._json['url']
            user_created_at = tweet.author._json['created_at']
            user_contributors_enabled = tweet.author._json[
                'contributors_enabled']
            user_time_zone = tweet.author._json['time_zone']
            user_protected = tweet.author._json['protected']
            user_default_profile = tweet.author._json['default_profile']
            user_is_translator = tweet.author._json['is_translator']

    if len(terms) > 1:
        print 'TODO'

if __name__ == '__main__':
    search_twit(search_terms)

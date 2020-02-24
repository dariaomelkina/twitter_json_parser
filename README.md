# Web App for Twitter 
*Main module: twitter_json_parser_task2.py* <br /> 

Parses given json file by its keys.
### Prerequisites
```
pip install flask
```
```
pip install folium
```
```
pip install geopy
```

### Example
```
This program parses json file with information about account's friends, got with Twitter API.
Please, enter the path to json file: twitter_data.json
Available keys: ['users', 'next_cursor', 'next_cursor_str', 'previous_cursor', 'previous_cursor_str', 'total_count']
Which key are you interested in? users
Your answer contains dictionaries, its length =  5
Do you want to access a certain elemet in the list?(Y/N) Y
Which element do you want?(number) 1
Available keys: ['id', 'id_str', 'name', 'screen_name', 'location', 'description', 'url', 'entities', 'protected', 'followers_count', 'friends_count', 'listed_count', 'created_at', 'favourites_count', 'utc_offset', 'time_zone', 'geo_enabled', 'verified', 'statuses_count', 'lang', 'status', 'contributors_enabled', 'is_translator', 'is_translation_enabled', 'profile_background_color', 'profile_background_image_url', 'profile_background_image_url_https', 'profile_background_tile', 'profile_image_url', 'profile_image_url_https', 'profile_banner_url', 'profile_link_color', 'profile_sidebar_border_color', 'profile_sidebar_fill_color', 'profile_text_color', 'profile_use_background_image', 'has_extended_profile', 'default_profile', 'default_profile_image', 'following', 'live_following', 'follow_request_sent', 'notifications', 'muting', 'blocking', 'blocked_by', 'translator_type']
Which key are you interested in? entities
Your answer contains dictionaries, number of dictionaries =  2
Do you want to access a certain dictionary?(Y/N) N
Your answer is a dictionary, do you want to access a certain key?(Y/N) N
Here is your answer:  ({'url': {'urls': [{'url': 'https://t.co/DnyXu6JwmD', 'expanded_url': 'http://IMAGINEPEACE.com', 'display_url': 'IMAGINEPEACE.com', 'indices': [0, 23]}]}, 'description': {'urls': []}}, 0)
```


## Author
*Daria Omelkina*
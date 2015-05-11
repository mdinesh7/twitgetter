# twitgetter
Get data from twitter

### config.py structure

```sh
from pymongo import MongoClient

# Note - these are dummy auth details, replace these with your's
consumer_key = 'abcddfjuif9899ew'
consumer_secret = 'Tjkdfjdkfhdifhdif89yghjj@/jfkdjfkdjfkjkjk'
access_token = '434884538-Yuidfkjfdh78jkdfl(hjhj34'
access_token_secret = 'jdfkljdfjdfku8ijrkJKLJBN87kjHlHjjsdkfjkdfjkd'

# Mongodb Connection
client = MongoClient('localhost', 27017)
db = client.toolsDb
collection = db.languages

search_terms = ["python", "javascript"]
```

### Usage
  - Install the dependencies
  - Create python script called config.py and copy paste the code above.
  - Enter your twitter api auth details in config.py
  - Enter the terms you want to track in search_terms list, which is available inside config.py
  - To start the program, type python get_tweets.py

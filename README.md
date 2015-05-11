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

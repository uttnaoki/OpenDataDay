#!/usr/bin/env python
# -*- coding: utf-8 -*-

from requests_oauthlib import OAuth1Session
import json

CK = '0CIwSJFoiv6QOIVbCusmR9AVS'                             # Consumer Key
CS = 'BCnPW0YjV0scOnrmzxiLdN1c50wBmIcrZ73QqJGEzVcMkW8WCF'         # Consumer Secret
AT = '4879432581-T7jBrbYonfUQ6IF56P71CK1OgMuPXYad322iPa9' # Access Token
AS = 'HiOg3GtFr25aZ1vZOHNqCxjpOrByZs62otVkOdfXq0o4z'         # Accesss Token Secert

# ツイート投稿用のURL
url = "https://api.twitter.com/1.1/statuses/home_timeline.json"

# ツイート本文
params = {}

# OAuth認証で POST method で投稿
twitter = OAuth1Session(CK, CS, AT, AS)
req = twitter.get(url, params = params)

# レスポンスを確認
if req.status_code == 200:
    timeline=json.loads(req.text)
    for tweet in timeline:
        print(tweet["text"])

    with open("test.json", "w") as f:
        json.dump(timeline, f, sort_keys = True, indent = 4)
else:
    print ("Error: %d" % req.status_code)

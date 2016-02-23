#!/usr/bin/env python
# -*- coding:utf-8 -*-

from requests_oauthlib import OAuth1Session
import json
import sys
### Constants
oath_key_dict = {
    "CK" : '0CIwSJFoiv6QOIVbCusmR9AVS',                             # Consumer Key
    "CS" : 'BCnPW0YjV0scOnrmzxiLdN1c50wBmIcrZ73QqJGEzVcMkW8WCF' ,        # Consumer Secret
    "AT" : '4879432581-T7jBrbYonfUQ6IF56P71CK1OgMuPXYad322iPa9' ,# Access Token
    "AS" : 'HiOg3GtFr25aZ1vZOHNqCxjpOrByZs62otVkOdfXq0o4z'
}

### Functions
def main():
    f = open("test2.txt", "w", encoding="UTF-8")
    tweets = tweet_search("マスキングテープ 発祥", oath_key_dict)
    for tweet in tweets["statuses"]:
        tweet_id = tweet['id_str']
        text = tweet['text']
        created_at = tweet['created_at']
        user_id = tweet['user']['id_str']
        user_description = tweet['user']['description']
        screen_name = tweet['user']['screen_name']
        user_name = tweet['user']['name']
        print("tweet_id:%s" % tweet_id)
        f.write(user_name)
        f.write(created_at)
        f.write("\n")
        f.write(text)
        f.write("\n\n\n\n\n\n")
    with open("test2.json", "w", encoding="UTF-8") as f:
        json.dump(tweets, f, sort_keys = True, indent = 4)
    return


def create_oath_session(oath_key_dict):
    oath = OAuth1Session(
    oath_key_dict["CK"],
    oath_key_dict["CS"],
    oath_key_dict["AT"],
    oath_key_dict["AS"]
    )
    return oath

def tweet_search(search_word, oath_key_dict):
    url = "https://api.twitter.com/1.1/search/tweets.json?"
    params = {
        "q": search_word,
        "lang": "ja",
        "result_type": "recent",
        "count": "100"
        }
    oath = create_oath_session(oath_key_dict)
    responce = oath.get(url, params = params)
    if responce.status_code != 200:
        return None
    tweets = json.loads(responce.text)
    return tweets

### Execute
if __name__ == "__main__":
    main()

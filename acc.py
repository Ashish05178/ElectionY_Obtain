from twitter import *
from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
from datetime import datetime, date, time, timedelta
from collections import Counter
import pandas as pd
import numpy as np 
import sys

consumerKey = ''
consumerSecret = ''
accessToken = ''
accessTokenSecret = ''
 
auth = OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
auth_api = API(auth)

twitter = Twitter(auth = OAuth(accessToken,

                  accessTokenSecret,

                  consumerKey,

                  consumerSecret))



user = "@manvendrakings"




results = twitter.statuses.user_timeline(screen_name = user)




a = []

for status in results:

    print("(%s) %s" % (status["created_at"], status["text"].encode("ascii", "ignore")))
    
data = pd.DataFrame(data=[status["text"] for status in results], columns=['Tweets'])

data['time']   = np.array([status["created_at"] for status in results])
data['tweet']   = np.array([status["text"] for status in results])

data.to_csv('firstresult4.csv')

    

# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 15:17:14 2019

@author: deeps
"""

#!/usr/bin/env python3

"""
import numpy as np
import pandas as pd
import pip

! pip install twitter
from twitter import Twitter
from twitter import OAuth


apikey='XnL8pCAcMHMIFMwW9mdcD9DSK'
apisecretkey='jmDiXeTytn9sCH44fbtPFfbwAxvEDdO8xWzdZp2gd4uvAfrf3K'
accesstoken='1103744573086597129-4bw6mdWHxlf922V8Dzd5x8NzVuwtSV'
accesstokensecret='ncXYufRwFUDyC93YfIFZpMrtf6bKV7eJNOeJTDCjiiwdJ'

oauth = OAuth(accesstoken,accesstokensecret,apikey,apisecretkey)
api = Twitter(auth=oauth)

#lets look at whats trending around the world
t_loc = api.trends.available()
print(t_loc)

from pandas.io.json import json_normalize  #converts it into pandas table

df_loc=json_normalize(t_loc)
df_loc
df_loc.country.value_counts()

dfNew=df_loc[df_loc['name'].str.contains('New')]
dfNew[['name','woeid']]
ny=dfNew.loc[dfNew.name=='New York','woeid']
ny
ny_trend = api.trends.place(_id=ny) #type is a series.

type(ny)
ny.values
ny.values[0]
ny_trend = api.trends.place(_id=ny.values[0])
ny_trend

########## Saving and Reading Objects ######################
import json
with open('ny_trend.json', 'w') as outfile:
    json.dump(ny_trend, outfile)

# Getting back the objects:
with open('ny_trend.json') as json_data:
    ny_trend_example = json.load(json_data)

############################################################


dfny=json_normalize(ny_trend)
dfny
type(dfny.trends)
dfny.trends.shape

dftrends=json_normalize(dfny.trends.values[0])
dftrends
dftrends.to_pickle('dftrends.pkl')
dftrends = pd.read_pickle('dftrends.pkl')

api.statuses.update(status="Their is an invasion at the border, someone get Jon Snow!!!")
mytweets=api.statuses.home_timeline()



dfmyt=json_normalize(mytweets)
dfmyt.to_pickle('dfmyt.pkl')
dfmyt=pd.read_pickle('dfmyt.pkl')
dd=dfmyt.loc[0]

mytweets1=api.statuses.home_timeline(count=5)
dfmyt1=json_normalize(mytweets1)

#Searching tweets on prarticular trending topics
dftrends.columns
dftrends.nlargest(5,'tweet_volume')[['name','tweet_volume']]

search_result = api.search.tweets(q='Modi',count = 200,tweet_mode='extended')

dfsr=json_normalize(search_result)
dfsr.to_pickle('dfsr.pkl')

dfst=json_normalize(dfsr.statuses.values[0])
df0=pd.DataFrame({'Value':dfst.loc[0]})

tjson=api.statuses.user_timeline(screen_name="realDonaldTrump",tweet_mode='extended')
dftrump=json_normalize(tjson)

tfollow=api.followers.ids(screen_name="realDonaldTrump")
dffol=json_normalize(tfollow)
dffol2=json_normalize(tfollow,'ids')
dffol2.to_pickle('dffol2.pkl')

dfst2=json_normalize(search_result,'statuses')

u0=api.users.lookup(user_id=dffol2.loc[0,0])
dfu0=json_normalize(u0)

mcuban=api.statuses.user_timeline(id=963973915256246272)










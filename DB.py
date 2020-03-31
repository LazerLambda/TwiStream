import pymongo

from datetime import datetime



class Tweet_DB:

    def __init__(self) -> (): 
        self.client = pymongo.MongoClient('localhost',27017) #"mongodb://localhost:27017/")
        db = self.client["covid_tweets"]
        self.coll = db["tweet_data"]


    def write(self,  tweet : dict) -> ():
        
        data = {
            'id' :          tweet['id'],
            'id_str' :      tweet['id_str'],
            'source' :      tweet['source'],
            'user'   : {
                'id'     :          tweet['user']['id'],
                'id_str' :          tweet['user']['id_str'],
                'name'   :          tweet['user']['name'],
                'screen_name':      tweet['user']['screen_name'],
                'location':         tweet['user']['location'],
                'description':      tweet['user']['description'],
                'followers_count':  tweet['user']['followers_count'],
                'friends_count' :   tweet['user']['followers_count'],
                'listed_count'  :   tweet['user']['listed_count'],
                'favourites_count': tweet['user']['favourites_count'],
                'statuses_count' :  tweet['user']['statuses_count'],
                'created_at' :      tweet['user']['created_at'],
            },
            'geo'   :       tweet['geo'],
            'coordinates':  tweet['coordinates'],
            'place':        tweet['place']
        }
        
        self.coll.insert_one(data)
        print("Inserted Data ", str(datetime.now()).replace(' ', '_'))


    def close(self) -> ():
        self.client.close()
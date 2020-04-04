import hashtags
import json
import os
import signal
import sys

from DB import Tweet_DB
from dotenv import load_dotenv
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener


load_dotenv()

run = True

class Tweet_Listener(StreamListener):

    def __init__(self, db):
        self.db = db

    def on_data(self, data):

        data = json.loads(data)
        self.db.write(data)
        
    def on_error(self, status):
        print(status)




if '__main__'==__name__:

    db = Tweet_DB()


    def signal_handler(sig, frame):
        global run
        run = False
        print('You pressed Ctrl+C!')
        db.close()
        print('Database connection closed')
        sys.exit(0)
    signal.signal(signal.SIGINT, signal_handler)



    listener    = Tweet_Listener(db)
    auth        = OAuthHandler(
        os.getenv('TWITTER_CONSUMER_KEY'),
        os.getenv('TWITTER_CONSUMER_SECRET')
    )
    auth.set_access_token(
        os.getenv('TWITTER_ACCESS_TOKEN'),
        os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
    )
    while run:
        try:
            stream = Stream(auth, listener)
            stream.filter(track=hashtags.HASHTAG_LIST)
        except Exception as e:
            print(e)
            print("An Error was thrown. Trying to reconnect...")

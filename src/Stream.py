
import tweepy


class Stream:

    def __init__(
        self,
        consumer_key: str,
        consumer_secret: str,
        access_token_key: str,
        access_token_secret: str,
        
        ):
        run:bool = True

        # open database
        self.client = pymongo.MongoClient('localhost',27017) #"mongodb://localhost:27017/")
        db = self.client["covid_tweets"]
        self.coll = db["tweet_data"]

    def open_db(self) -> None:
        pass

    def close_db(self) -> None:
        pass

    def start(self) -> None:
       
        exp_counter = 1
        while self.run:
            if exp_counter > 300:
                exp_counter = 1
            else:
                time.sleep(exp_counter)
                exp_counter = exp_counter ** 2
            try:
                stream = Stream(auth, listener)
                stream.filter(track=hashtags.HASHTAG_LIST)
            except Exception as e:
                exp_counter = 1
                print("%s\n\n\t'->An Error was thrown. Trying to reconnect..." % str(e))
            pass

    def interrupt(self) -> None:
        self.run = False
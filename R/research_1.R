

# imports
library(mongolite)


db <- mongo(collection = "tweet_data", db= "covid_tweets", url = "mongodb://localhost:27017/")

length(db$aggregate(
  
))
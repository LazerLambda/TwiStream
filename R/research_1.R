

# imports
library(cld3)
library(dplyr)
library(forcats)
library(ggplot2)
library(mongolite)


db <- mongo(collection = "tweet_data", db= "covid_tweets", url = "mongodb://localhost:27017/")
query <- '{"text" : { "$regex" : ".*Trump.*",  "$options" : "i" }}'


# get all tweets related to  (keyword Trump)
data_trump <- db$find(query)$text

# 
ratio <- length(data_trump) / length(all_data$text)

language_vector <- c(1:length(data_trump))
for( val in 1:length(data_trump)){
  language_vector[val] <- detect_language(data_trump[val])
}

data <- data.frame("lang"=language_vector)
cleared <- na.omit(data)

title_str <- "Languages used in tweets related to Donald Trump and the Novel Coronavirus \nin between Mo Apr 06 17:19:49 and "
title_str <- paste(title_str,format(Sys.time(), "%a %b %d %X %Y"), sep=" ")

ggplot(cleared, aes(fct_infreq(lang))) +
  geom_bar(width=0.4, position = position_dodge(width=0.5)) + 
  scale_y_continuous(trans='log10') +
  scale_x_discrete(labels = function(labels) {
    fixedLabels <- c()
    for (l in 1:length(labels)) {
      fixedLabels[l] <- paste0(ifelse(l %% 2 == 0, '', '\n'), labels[l])
    }
    return(fixedLabels)
  }) +
  labs(title=title_str,
        x ="Languages", y = "Amount", subtitle = "Tweets containing the string \"Donald Trump\" and at least one these Hashtag: #Covid19 #Coronavirus #Corona #Virus\nLog scale")
  
  #coord_flip()
  
  #theme(axis.title.x = element_text(margin = margin(t = 40, r = 100, b = 100, l = 100)))


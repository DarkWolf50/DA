#Consider the following review message.Perform sentiment analysis on the message.
#1.I purchased headphones online.I am very happy with th product.
#2.I saw the movie yesterday.The animations was really good but the script was ok.

import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
vader_analyzer=SentimentIntensityAnalyzer()
text1=("I purchased headphones online.I am very happy with th product")
result1=vader_analyzer.polarity_scores(text1)
print(result1)
if(result1['compound']>=0.5):
    print("Overall rating For Sentence Is Positive")
elif(result1['compound']<=0.5):
    print("Overall rating For Sentence Is Negative")
else:
    print("Overall rating For Sentence Is Neutral")

text2=("I saw the movie yesterday.The animation was really good but the script was ok.")
result2=vader_analyzer.polarity_scores(text2)
print(result2)
if(result2['compound']>=0.5):
    print("Overall rating Is positive")
elif (result2['compound'] <= 0.5):
    print("Overall rating Is Negative")
else:
    print("Overall rating Is Neutral")
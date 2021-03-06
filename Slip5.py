#Consider the following review messages. Perform sentiment analysis on the messages.
#i) I enjoy listening to music.
#ii) I take a walk in the park everyday.

import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
vader_analyzer=SentimentIntensityAnalyzer()
text1=("I enjoy listening to music.")
result1=vader_analyzer.polarity_scores(text1)
print(result1)
if(result1['compound']>=0.5):
    print("Overall rating For Sentence Is Positive")
elif(result1['compound']<=0.5):
    print("Overall rating For Sentence Is Negative")
else:
    print("Overall rating For Sentence Is Neutral")

text2=("I take a walk in the park everyday.")
result2=vader_analyzer.polarity_scores(text2)
print(result2)
if(result2['compound']>=0.5):
    print("Overall rating Is positive")
elif (result2['compound'] <= 0.5):
    print("Overall rating Is Negative")
else:
    print("Overall rating Is Neutral")
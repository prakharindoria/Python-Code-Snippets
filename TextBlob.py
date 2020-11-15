from textblob import TextBlob

#Input
Feedback1="The hotel was great"

#Sentiment
blob1=TextBlob(Feedback1).sentiment

#Check
if blob1[0]>=0.5:
    print("Positive")
else:
    print("Negative")



from textblob import TextBlob
from newspaper import Article
# import nltk
# nltk.download('punkt_tab')

# For URL
# url = 'https://www.bbc.com/news/articles/ckgr71z0jp4o'
# article = Article(url)

# article.download()
# article.parse()
# article.nlp()

# text = article.summary
# print(text)

# for texts
with open('sample.txt', 'r') as f:
    text = f.read()
    
blob = TextBlob(text)
sentiment = blob.sentiment.polarity # -1 to 1
print(sentiment)
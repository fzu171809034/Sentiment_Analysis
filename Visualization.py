import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_excel('Analysis.xlsx')
data = data[::-1]
print(data)

positive_count = (data['compound']>0).sum()
negative_count = (data['compound']<0).sum()
neutral_count = (data['compound']==0).sum()


counts = [positive_count, negative_count, neutral_count]
labels = ['Positive', 'Negative', 'Neutral']

plt.figure(figsize=(10,10))
plt.pie(counts, labels=labels, autopct='%1.1f%%')
plt.title('Sentiment Analysis')
plt.savefig('Chart/Sentiment Analysis.png')
plt.show()

data['created_at'] = pd.to_datetime(data['created_at'])
data['time'] = data['created_at'].dt.time
data['time_str'] = data['time'].astype(str)

plt.figure(figsize=(20,10))
plt.plot(data['time_str'], data['compound'])
plt.xticks(rotation=45)
plt.title('Sentiment Changes')
plt.savefig('Chart/Sentiment_Changes.png')
plt.show()


import pandas as pd

# Load dataset with no headers and set column names
df = pd.read_csv("amazon_product_review.csv", header=None)
df.columns = ['userId', 'productId', 'rating', 'timestamp']

# Ensure rating is numeric
df['rating'] = pd.to_numeric(df['rating'], errors='coerce')

# Drop rows with missing or invalid ratings
df = df.dropna(subset=['rating'])

# Convert numeric ratings into sentiment labels
def rating_to_sentiment(r):
    if r >= 4:
        return 'Positive'
    elif r <= 2:
        return 'Negative'
    else:
        return 'Neutral'

df['sentiment'] = df['rating'].apply(rating_to_sentiment)

# Show sentiment distribution
print("Sentiment Distribution:")
print(df['sentiment'].value_counts())

# Show some sample sentiment-tagged data
print("\nSample Sentiment Data:")
print(df[['userId', 'productId', 'rating', 'sentiment']].head(10))

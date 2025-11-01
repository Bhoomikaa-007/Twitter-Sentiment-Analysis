import tweepy
from textblob import TextBlob
import pandas as pd
import os
import time

# Load Bearer Token securely
BEARER_TOKEN = os.getenv("BEARER_TOKEN")

# Initialize Tweepy client
client = tweepy.Client(bearer_token=BEARER_TOKEN)

def fetch_tweets_v2(search_term, no_of_tweets):
    """
    Fetch tweets from Twitter API v2.
    If API fails (rate limit or 401), uses offline demo tweets.
    """
    tweets_data = []
    try:
        print("Fetching tweets...")
        tweets = client.search_recent_tweets(
            query=search_term,
            max_results=min(no_of_tweets, 100),
            tweet_fields=["text", "author_id", "created_at"]
        )
        if tweets.data:
            for tweet in tweets.data:
                tweets_data.append({
                    "text": tweet.text,
                    "author_id": tweet.author_id,
                    "created_at": tweet.created_at
                })
        else:
            print("No tweets found. Using sample data.")
            return load_demo_tweets()
    except tweepy.TooManyRequests:
        print("Rate limit hit! Waiting 15 mins...")
        time.sleep(15 * 60)
        return fetch_tweets_v2(search_term, no_of_tweets)
    except Exception as e:
        print(f"Error fetching tweets: {e}")
        print("⚙️ Switching to offline demo data.")
        return load_demo_tweets()
    return tweets_data

def analyze_sentiment(tweet_text):
    """Return sentiment category (Positive, Neutral, Negative)."""
    analysis = TextBlob(tweet_text)
    polarity = analysis.sentiment.polarity
    if polarity > 0:
        return "Positive"
    elif polarity == 0:
        return "Neutral"
    else:
        return "Negative"

def load_demo_tweets():
    """Load local tweets for demo mode."""
    return pd.read_csv("sample_tweets.csv").to_dict(orient="records")

def main():
    search_term = input("Enter the keyword or hashtag to search for: ")
    no_of_tweets = int(input("Enter the number of tweets to fetch: "))

    tweets = fetch_tweets_v2(search_term, no_of_tweets)
    df = pd.DataFrame(tweets)
    df["sentiment"] = df["text"].apply(analyze_sentiment)

    output_file = "sentiment_analysis_results.csv"
    df.to_csv(output_file, index=False)
    print(f"Analysis complete! Results saved to {output_file}")
    print(df.head())

if __name__ == "__main__":
    main()


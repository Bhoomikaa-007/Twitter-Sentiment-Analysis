# 🧠 Twitter Sentiment Analysis using Tweepy and TextBlob

This project performs **sentiment analysis** on tweets fetched from the **Twitter API (v2)**.  
Given a **keyword or hashtag**, it retrieves recent tweets and classifies them as **Positive**, **Negative**, or **Neutral** using **TextBlob** for natural language processing.

---

## 🚀 Features
- 🔍 **Keyword/Hashtag Search:** Fetch tweets in real-time based on user input.  
- 💬 **Sentiment Classification:** Automatically detects polarity and assigns sentiment labels.  
- 📊 **Export to CSV:** Saves analyzed tweets to `sentiment_analysis_results.csv`.  
- ⚠️ **Error Handling:** Automatically switches to offline/demo mode if API errors occur (e.g., rate limit, unauthorized access).  
- 🧾 **Simple CLI Interface:** Enter keyword and number of tweets easily via the terminal.  

---

## 🧩 Tech Stack
**Language:** Python  

**Libraries Used:**
- [`tweepy`](https://www.tweepy.org/) – Access Twitter API v2  
- [`textblob`](https://textblob.readthedocs.io/) – Sentiment analysis  
- [`pandas`](https://pandas.pydata.org/) – Data manipulation and storage  
- [`python-dotenv`](https://pypi.org/project/python-dotenv/) – Secure environment variable handling  

---

## ⚙️ How It Works
1. User enters a keyword or hashtag and number of tweets to fetch.  
2. The script authenticates using **Twitter API credentials** stored in the `.env` file.  
3. Tweets are fetched using Tweepy and analyzed using **TextBlob** for sentiment polarity.  
4. Each tweet is categorized as:
   - **Positive** (polarity > 0)  
   - **Negative** (polarity < 0)  
   - **Neutral** (polarity = 0)  
5. Results are displayed in the console and exported to a CSV file for further analysis.

---

## 📁 Project Structure

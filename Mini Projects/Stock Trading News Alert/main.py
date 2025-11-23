'''Module that gets the API's needed'''
import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
NEWS_PIECES = 3
STOCK_KEY = "71NNSYLZ85SP33J6"
STOCK_URL = "https://www.alphavantage.co/query"
NEWS_KEY = "b0557efc81ae48a69d303f769bc397b7"
NEWS_URL = "https://newsapi.org/v2/everything"
ACCOUNT_SID = "AC73fae689870200474455d5a14fdd4f5d"
AUTH_TOKEN = "c99f114c08a2d7b9c504e80e3ce48fce"
## STEP 1: Use https://www.alphavantage.com
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outputsize": "compact",
    "apikey": STOCK_KEY
}
response = requests.get(url=STOCK_URL, params=stock_parameters, timeout=10)
stock_data = response.json()["Time Series (Daily)"]
stock_data_list = [value for (key, value) in stock_data.items()]
yesterday_price = float(stock_data_list[0]["4. close"])
bef_yesterday_price = float(stock_data_list[1]["4. close"])
difference_perc = ((yesterday_price - bef_yesterday_price)/bef_yesterday_price) * 100
if difference_perc <= -1 or difference_perc >= 1:
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
    news_parameters = {
        "q":COMPANY_NAME,
        "sortBy":"popularity",
        "apiKey": NEWS_KEY,
        "language": "en"
    }
    news_response = requests.get(url=NEWS_URL, params=news_parameters, timeout=10)
    news_response.raise_for_status()
    articles = news_response.json()["articles"]
    three_articles = articles[:3]
    print(three_articles)
## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
    formatted_articles = [f"Headline: {article['title']} \nBrief: {article['description']}" for article in three_articles]
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    if difference_perc > 0:
        EMOJI = "🔺"
    else:
        EMOJI = "🔻"
    for article in formatted_articles:
        message = client.messages.create(
            messaging_service_sid='MGf9fa87b8ceae0c94621b6e8ae39617ab',
            body=f"{STOCK}: {EMOJI}{difference_perc:.2f}\n"
            f"{article}",
            to="+5511934262043"
        )   
    print(message.status)
#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


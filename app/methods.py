import json
import yfinance as yf


def load_json_data():
    with open("shares.json") as json_file:
        return json.load(json_file)


def price_to_share_value(purchase_price, share_amount):
    return purchase_price * share_amount


def get_total_portfolio_worth(json_data):
    """Get total value of portfolio rounded to 2 decimal places - no individual ticker details"""
    total = 0
    for i in json_data:
        # gets into individual ticker
        for j in json_data[i]:
            # gets into individual share purchase
            total += price_to_share_value(j["price"], j["share_amount"])
    return total


def get_ticker_list(json_data):
    ticker_list = []
    for ticker in json_data:
        ticker_list.append(ticker)
    return ticker_list


def get_total_worth_for_ticker(ticker, json_data):
    total = 0.00
    if ticker in json_data:
        for purchase in json_data.get(ticker):
            total += price_to_share_value(purchase["price"], purchase["share_amount"])
        total = format(total, ".2f")
        print(f"{ticker}: ${total}")


def get_ticker_closing_price(ticker):
    ticker_detail = yf.Ticker(ticker)
    ticker_data = ticker_detail.history()
    return ticker_data["Close"].iloc[-1]

#def_get_profit_loss_for_ticker(ticker)
#   ticker_last_quote = get_ticker_closing_price(ticker)
#         print("Most recent META price: $" + str(meta_last_quote))
#         print("Current profit/loss: $" + str(round(float(meta_last_quote - 94),2)))
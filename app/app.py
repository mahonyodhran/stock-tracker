from methods import (
    get_ticker_list,
    get_total_portfolio_worth,
    get_total_worth_for_ticker,
    load_json_data,
)

json_data = load_json_data()
tickers = get_ticker_list(json_data)

for ticker in tickers:
    get_total_worth_for_ticker(ticker, json_data)

portfolio_value = format(get_total_portfolio_worth(json_data), ".2f")
print(f"Portfolio Value: ${portfolio_value}")

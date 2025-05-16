# The above data is data for prebid auctions.
# There are bidders who receive requests for placing ads,
# they respond to these requests with a bid and the highest bid wins the auction.
# Analyse the dataset to answer which bidder has the highest win rate (wins / total_bid).

import pandas as pd

auction_data = pd.read_csv(r"D:\vscode-data\Ascenedeum_int\analysis_id(in).csv")


# Approach 1
result = (
    auction_data.groupby("bidder")
    .agg({"prebid_win_count": "sum", "response_count": "sum"})
    .reset_index()
)

result["win_rate_pre"] = (result["prebid_win_count"] / result["response_count"]) * 100

result.sort_values(by="win_rate_pre", ascending=False, inplace=True)

result = (
    auction_data.groupby("bidder")
    .agg({"prebid_win_count": "sum", "response_count": "sum"})
    .reset_index()
)

print(result.head(2))

# Approach 2


result2 = (
    auction_data.groupby("bidder")
    .agg({"response_count": "sum", "prebid_win_count": "sum", "win_count": "sum"})
    .reset_index()
)

result2["mean_win_count"] = (result2["prebid_win_count"] + result2["win_count"]) / 2

result2["win_rate_mean"] = (result2["mean_win_count"] / result2["response_count"]) * 100

result2.drop(columns=["mean_win_count"], inplace=True)

result2.sort_values(by="win_rate_mean", ascending=False, inplace=True)

print(result2.head(2))
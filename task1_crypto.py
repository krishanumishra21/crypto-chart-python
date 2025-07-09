import requests
import matplotlib.pyplot as plt

# coins
coin_list = ["bitcoin", "ethereum", "ripple", "solana", "dogecoin"]

# API 
api_url = "https://api.coingecko.com/api/v3/coins/markets"
query = {
    "vs_currency": "inr",
    "ids": ",".join(coin_list)
}


res = requests.get(api_url, params=query)    # Getting data
coins = res.json()

# Prepare data for chart
labels = []
values = []

for c in coins:
    labels.append(c["name"].capitalize())
    values.append(c["current_price"])
    print(f"{c['name'].capitalize()} : ₹{c['current_price']}")

# Plot chart
plt.figure(figsize=(8, 5))
plt.bar(labels, values, color="black")
plt.title("Crypto Prices in INR", fontsize=14, fontweight='bold')
plt.xlabel("Coins")
plt.ylabel("Price (₹)")
plt.grid(axis="y", linestyle="--", alpha=0.3)
#to show
plt.savefig("chart.png")
plt.show()

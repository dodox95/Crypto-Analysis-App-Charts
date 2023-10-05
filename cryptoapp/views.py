# cryptoapp/views.py

import requests
import pandas as pd
import matplotlib.pyplot as plt
import mpld3
import matplotlib
from mpld3 import plugins
from django.shortcuts import render

# Ustalanie backendu Matplotlib na 'Agg' dla kompatybilności z Django
matplotlib.use('Agg')

def get_crypto_data(crypto_name):
    url = f"https://api.coingecko.com/api/v3/coins/{crypto_name}/market_chart?vs_currency=usd&days=30&interval=daily"
    data = requests.get(url).json()
    prices = data['prices']
    df = pd.DataFrame(prices, columns=['time', 'price'])
    df['time'] = pd.to_datetime(df['time'], unit='ms')
    return df


def crypto_chart(request, crypto_name="bitcoin"):
    df = get_crypto_data(crypto_name)
    fig, ax = plt.subplots(figsize=(10,5))
    lines = ax.plot(df['time'], df['price'], label=crypto_name)
    ax.set_title(f'Price of {crypto_name} for last 30 days')
    ax.set_xlabel('Date')
    ax.set_ylabel('Price (in USD)')
    ax.legend()

    # Dodaj wtyczkę Tooltip - jest to ten fragment, o którym mówimy:
    labels = list(df["price"])
    tooltips = plugins.PointLabelTooltip(lines[0], labels=labels)
    plugins.connect(fig, tooltips)

    chart = mpld3.fig_to_html(fig)
    plt.close(fig)
    return render(request, 'crypto_chart.html', {'crypto_chart': chart})


def crypto_list(request):
    query = request.GET.get('q')
    cryptos = get_top_cryptos()

    if query:
        cryptos = [crypto for crypto in cryptos if query.lower() in crypto.lower()]

    return render(request, 'crypto_list.html', {'cryptos': cryptos})



def get_top_cryptos():
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&limit=100&sparkline=false&price_change_percentage=24h"
    data = requests.get(url).json()
    return [coin['id'] for coin in data]

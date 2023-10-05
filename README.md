# Crypto Analysis App

The Crypto Analysis App allows users to view the price charts of various cryptocurrencies for the last 30 days. The app fetches real-time data from the CoinGecko API and displays it in a visually appealing format using Matplotlib and D3.js. Users can also search for specific cryptocurrencies.

## Features

- **Cryptocurrency Listing:** View a list of the top cryptocurrencies.
- **Price Charts:** Visualize the price of a selected cryptocurrency over the last 30 days.
- **Search:** Users can search for specific cryptocurrencies from the main list.

## Templates

The app consists of 3 main templates:

- `base.html`: This serves as the main layout template for the app, including necessary CSS and JS links.
- `crypto_list.html`: Shows a list of available cryptocurrencies with search functionality.
- `crypto_chart.html`: Displays a detailed price chart for a selected cryptocurrency.

## Implementation

The main logic is in `views.py`:

- `get_crypto_data(crypto_name)`: Fetches the 30-day price data for a given cryptocurrency.
- `crypto_chart(request, crypto_name="bitcoin")`: Generates the price chart for the selected cryptocurrency.
- `crypto_list(request)`: Displays a list of the top cryptocurrencies, with search functionality.

## Configuration

The app's configuration is in `settings.py`. Make sure to set your `SECRET_KEY` in an `.env` file and use the `decouple` library to fetch it for security.

## Routes

Defined in `urls.py`, the app has two main routes:

- `<str:crypto_name>/`: Displays the price chart for a selected cryptocurrency.
- `/`: Lists the top cryptocurrencies with search functionality.

## Getting Started

1. Make sure you have Django and the necessary libraries installed.
2. Clone the repository.
3. Set up your `.env` file with the `SECRET_KEY`.
4. Run `python manage.py runserver` to start the development server.

## Dependencies

- Django
- Requests
- Pandas
- Matplotlib
- mpld3
- Decouple

## Future Enhancements

- Add more detailed analyses for each cryptocurrency.
- Integrate more data sources apart from CoinGecko.


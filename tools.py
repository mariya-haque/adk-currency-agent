import requests


def get_exchange_rate(
    currency_from: str = "USD",
    currency_to: str = "EUR",
    currency_date: str = "latest",
):
    """
    Retrieve the exchange rate between two currencies.

    Args:
        currency_from: Base currency (e.g. USD)
        currency_to: Target currency (e.g. PKR)
        currency_date: Date in YYYY-MM-DD format or "latest"

    Returns:
        A dictionary containing the exchange rate information.
    """

    url = f"https://api.frankfurter.app/{currency_date}"

    params = {
        "from": currency_from.upper(),
        "to": currency_to.upper(),
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()

        data = response.json()

        return {
            "success": True,
            "base_currency": data.get("base"),
            "target_currency": currency_to.upper(),
            "date": data.get("date"),
            "exchange_rate": data.get("rates", {}).get(currency_to.upper()),
        }

    except requests.exceptions.RequestException as e:
        return {
            "success": False,
            "error": str(e),
        }
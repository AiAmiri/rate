import requests
from bs4 import BeautifulSoup
from .models import KhorasanRate
from .models import SaraiRate
from .models import DaAfgRate
from decimal import Decimal, InvalidOperation
from django.utils import timezone


def scrape_rates():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }

    urls = {
        'khorasan': 'https://sarafi.af/en/exchange-rates/khorasan-market',
        'sarai': 'https://sarafi.af/en/exchange-rates/sarai-shahzada',
        'da_afg': 'https://sarafi.af/en/exchange-rates/da-afg-bank'
    }


    for market, url in urls.items():
        try:
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.content, 'html.parser')
            table = soup.find("table", class_="homeRates exchangeRatesTable mb-4")
            if not table:
                print(f"No rates table found for {market} at {url}")
                continue
            tbody = table.find("tbody")
            if not tbody:
                print(f"No table body found for {market} at {url}")
                continue
            rows = tbody.find_all("tr")
            
            for row in rows:
                try:
                    try:
                        currency = row.find("td").find("b").get_text(strip=True)
                    except AttributeError:
                        print("Skipping row due to missing currency data.")
                        continue

                    try:
                        buy_rate = row.find("b", class_="buyRate").get_text(strip=True)
                    except AttributeError:
                        buy_rate = None  # Set to None if missing

                    try:
                        sell_rate = row.find("b", class_="sellRate").get_text(strip=True)
                    except AttributeError:
                        sell_rate = None  # Set to None if missing
                        
                    time = None
                    time_td = row.find("td", class_="time")
                    if time_td:
                        time = time_td.get_text(strip=True)
                    #change = row.find("b", class_=["up", "down"]).get_text(strip=True)
                    
                    change_tag = row.find("b", class_=["up", "down"])
                    up, down = None, None
                    if change_tag:
                        value_text = change_tag.get_text(strip=True).replace("%", "")  # Remove the '%' symbol
                        value = _to_decimal(value_text)
                        if "up" in change_tag.get("class", []):  # Check if the class contains 'up'
                            up = value
                        elif "down" in change_tag.get("class", []):  # Check if the class contains 'down'
                            down = value


                    # Save data to the appropriate model
                    buy_dec = _to_decimal(buy_rate)
                    sell_dec = _to_decimal(sell_rate)
                    if market == 'khorasan':
                        KhorasanRate.objects.update_or_create(
                            currency=currency,
                            defaults={
                                'buying_rate': buy_dec,
                                'selling_rate': sell_dec,
                                'up': up,
                                'down': down,
                                'updated_time': time,
                                'timestamp': timezone.now(),
                            },
                        )
                    elif market == 'sarai':
                        SaraiRate.objects.update_or_create(
                            currency=currency,
                            defaults={
                                'buying_rate': sell_dec if False else buy_dec,  # keep explicit for readability
                                'selling_rate': sell_dec,
                                'up': up,
                                'down': down,
                                'updated_time': time,
                                'timestamp': timezone.now(),
                            },
                        )
                    elif market == 'da_afg':
                        DaAfgRate.objects.update_or_create(
                            currency=currency,
                            defaults={
                                'buying_rate': buy_dec,
                                'selling_rate': sell_dec,
                                'up': up,
                                'down': down,
                                'updated_time': time,
                                'timestamp': timezone.now(),
                            },
                        )
                    
                    print(f"Currency: {currency}, Buy: {buy_dec}, Sell: {sell_dec}, Up: {up}, Down: {down}, Time: {time}")
                
                except Exception as e:
                    print(f"Error saving data for {market}: {e}")

        except Exception as e:
            print(f"Error scraping {market}: {e}")


def _to_decimal(value):
    """
    Convert a scraped numeric string like '74.50' or '74,50' to Decimal.
    Returns None for invalid/empty values.
    """
    if value is None:
        return None
    if isinstance(value, (int, float, Decimal)):
        try:
            return Decimal(str(value))
        except InvalidOperation:
            return None
    text = str(value).strip()
    if text in ("", "-", "—", "N/A", "None"):
        return None
    # Remove common thousands separators
    text = text.replace(",", "").replace("\u200f", "")  # remove RTL mark if present
    # Handle possible non-breaking spaces
    text = text.replace("\xa0", "")
    try:
        return Decimal(text)
    except InvalidOperation:
        return None

import requests # Core library used for making HTTP requests to external APIs

def get_crypto_price(coin_id):
    """
    Fetches the current price of a cryptocurrency in EUR using the CoinGecko API.
    This function demonstrates API integration and data validation.
    """
    # Constructing the API endpoint URL using f-strings for dynamic coin IDs 
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=eur"
    
    try:
        # Performing a GET request to the specified URL 
        response = requests.get(url)
        
        # QA Best Practice: Always verify the HTTP status code before processing data.
        # 200 means the request was successful; anything else indicates an issue.
        if response.status_code != 200:
            return f"Error: Server returned status code {response.status_code}"
            
        # Parsing the raw response content into a Python dictionary (JSON format) 
        data = response.json()
        
        # Negative Testing Check: Ensure the requested key exists in the returned JSON 
        # This prevents the script from crashing if an invalid coin ID is passed.
        if coin_id in data:
            price = data[coin_id]['eur']
            return price
        else:
            return None
            
    except requests.exceptions.RequestException as e:
        # Error Handling: Catches network issues like timeouts or DNS failures
        return f"Connection error: {e}"

def main():
    """
    Main entry point of the script. 
    Iterates through a predefined list of assets and displays their current value.
    """
    print("--- CryptoPulse: Python API Tracker v1.0 ---")
    
    # List of coin IDs defined by the CoinGecko API documentation
    # We use specific IDs like 'binancecoin' for BNB or 'ripple' for XRP
    crypto_assets = [
        'bitcoin', 'ethereum', 'tether', 'ripple', 'solana', 
        'binancecoin', 'cardano', 'dogecoin', 'tron', 'polkadot'
    ]
    
    # Iterating through the asset list to perform 10 consecutive API calls
    # Note: Frequent requests may trigger Rate Limiting on public APIs
    for asset in crypto_assets:
        price = get_crypto_price(asset)
        
        # Type Validation: Ensuring the received data is a number before formatting
        if isinstance(price, (int, float)):
            # Formatting used for professional terminal output:
            # :<12 - Left-align the name within 12 characters
            # :>10,.2f - Right-align price with 2 decimals and a thousands separator
            print(f"Current price for {asset.capitalize():<12}: {price:>10,.2f} EUR")
        else:
            # Fallback message for failed data retrieval or API errors
            print(f"Data for {asset.capitalize():<12}: Status Offline/Error")

# Standard Python boilerplate to ensure the script runs only when executed directly
if __name__ == "__main__":
    main()

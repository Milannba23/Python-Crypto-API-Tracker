# Python Crypto API Tracker v1.0

## Description
This is a professional Python-based cryptocurrency tracking tool that integrates with the **CoinGecko API**. It demonstrates core QA Engineering principles, including API lifecycle management, data validation, and robust error handling.

## Key Features
- [cite_start]**Real-time Data Retrieval**: Fetches current prices for 10 major cryptocurrencies in EUR[cite: 36, 43].
- [cite_start]**API Robustness**: Validates HTTP status codes (200 OK) before processing data[cite: 1, 15].
- [cite_start]**Negative Testing**: Implements checks for invalid coin IDs to prevent application crashes[cite: 7, 15].
- [cite_start]**Professional Error Handling**: Uses `try-except` blocks to manage network timeouts or server outages[cite: 8].

## Tech Stack
- **Language**: Python 3.x
- [cite_start]**Libraries**: `requests` (v2.31.0 or newer) [cite: 1, 19]
- [cite_start]**API Source**: CoinGecko [cite: 2]

## Installation
1. Clone the repository.
2. Install dependencies:
   
   pip install -r requirements.txt
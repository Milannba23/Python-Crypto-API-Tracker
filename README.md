# Python Crypto API Tracker v1.0

## 📝 Description
This is a professional Python-based cryptocurrency tracking tool that integrates with the **CoinGecko API**. It demonstrates core QA Engineering principles, including API lifecycle management, data validation, and robust error handling.

## 🧪 QA Engineering & Testing Highlights
This project was built with a focus on software quality and reliability:
- [cite_start]**API Robustness**: Validates HTTP status codes (200 OK) before processing data[cite: 1].
- **Data Integrity**: Implements type-checking (`isinstance`) to verify that price data is a number.
- **Negative Testing**: Includes logic to handle invalid coin IDs gracefully.
- **Error Management**: Uses `try-except` blocks to manage network-level exceptions.

## 🛠 Tech Stack
- **Language**: Python 3.x
- [cite_start]**Libraries**: `requests` (v2.31.0 or newer) [cite: 1]
- **API Source**: [CoinGecko API](https://www.coingecko.com/en/api)

## ⚙️ Installation & Usage
1. **Clone the repository**:
   
   git clone [https://github.com/Milannba23/Python-Crypto-API-Tracker.git](https://github.com/Milannba23/Python-Crypto-API-Tracker.git)

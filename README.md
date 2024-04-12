# Amazon Price Tracker

## Overview
This Python script scrapes the price of a specific product on Amazon and sends an email notification if the price drops below a specified threshold. It utilizes BeautifulSoup for web scraping, requests for sending HTTP requests, and smtplib for sending emails.

## Prerequisites
- Python 
- BeautifulSoup (`pip install beautifulsoup4`)
- Requests (`pip install requests`)
- lxml (`pip install lxml`)
- smtplib (built-in with Python)

## Configuration
1. Set up a Gmail account to use for sending emails.
2. Enable "less secure app access" for the Gmail account.
3. Replace `"YOUR_EMAIL"` with your Gmail email address.
4. Replace `"YOUR_PASSWORD"` with the password of your Gmail account.
5. Replace `"YOUR_SMTP_ADDRESS"` with the SMTP server address of your email provider. For Gmail, it's `"smtp.gmail.com"`.

## Usage
1. Replace the URL in the `requests.get()` function with the Amazon product page URL of the product you want to track.
2. Customize the `BUY_PRICE` variable to set your desired price threshold.
3. Run the Python script `amazon_price_tracker.py`.
4. The script will scrape the product price from the Amazon page, compare it with the threshold, and send an email notification if the price drops below the threshold.

## Notes
- Ensure that the product page HTML structure remains consistent. Any changes to the page layout may require updates to the script.
- This script is for educational and personal use only. Use it responsibly and respect Amazon's terms of service.
- Adjust the frequency of running the script based on your needs. Running it too frequently might trigger anti-scraping mechanisms.


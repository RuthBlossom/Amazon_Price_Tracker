

# Import necessary libraries
from bs4 import BeautifulSoup
import requests
import lxml
import smtplib

# Define headers to mimic a browser request
# Headers are defined to mimic a browser request. This is often needed when scraping websites to avoid being blocked or getting inaccurate results.
header = {
    'Accept-Language': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                        "Chrome/118.0.0.0 Safari/537.36",
    'User-Agent': "en-US,en;q=0.9"
}

# Send a GET request to the Amazon product page URL
# A GET request is sent to the Amazon product page URL using requests.get(). The headers are passed along with the request to make it look like a request from a regular browser.
response = requests.get("https://www.amazon.com/ORIFANTOU-Polyhedral-Dungeons-Dragons-Playing/dp/B0CJFMN9T2/ref=sr_1_45?crid=2OJADJRKVX267&dib=eyJ2IjoiMSJ9.7k0LCS3I-CD9FtO2YbWSco2o1DfPH5I5fmSBjxe0wyPHuN7HDhn4g7LO5IzzJJ76eZE9rYIIC8gTEDL0Uic3NSTl-2YJHxhj1eYXYA-IcikwCPkVxty6Dgjzd9kpcxpKAzkti5GxNKQVWyAelaLCDroRMnVnoF_8hlju4boR7mxMlSrVPSpwTnM6j2fWnN2H-Dc85J-fiGkgVLg6mpreD3MEsZ322iob7ttiDoMr4Q3-ieBwHzwo_A-iM4SITDHjq5NEMTPL4zLY7WcP27FELRtXnFmr7B2GIRXRX1Kd0J8.3V_OKJyL_a5csf1x3DM9-FOdAdu2y99wzMygNFJU_Pc&dib_tag=se&keywords=dungeons%2Band%2Bdragons%2Bdice&qid=1710495660&sprefix=dungeons%2B%2Caps%2C380&sr=8-45&th=1",
                        headers=header)

# Parse the HTML content of the response using BeautifulSoup
# The HTML content of the response is parsed using BeautifulSoup, specifying the parser as lxml.
soup = BeautifulSoup(response.text, "lxml")

# Find the price of the product by searching for the appropriate HTML tag and class
# Using BeautifulSoup's find() method, it searches for a <span> tag with the class "a-offscreen". This class typically contains the price of the product on Amazon.
price = soup.find("span", class_="a-offscreen").get_text()

# The price is extracted as a string using get_text(), including the currency symbol.
# Remove the currency symbol and convert the price to a float
# The currency symbol is removed from the price string using slicing (price[1:]), and the result is converted to a float using float().
price = float(price[1:])

# Print the price
print(price)

# When you use .find(class_="a-offscreen"), it might not always return exactly what you're expecting because the "a-offscreen" class might be used for other elements on the page as well,
# not just for the price. This can lead to extracting more than just the price.

# To ensure you're specifically getting the price, you can try finding an element that directly corresponds to the price tag. On Amazon product pages, the price is often located within a <span> tag with the class "priceBlockBuyingPriceString" for the main price or "a-offscreen" for secondary prices.

# Find and print the title of the product
title = soup.find(id="productTitle").get_text().strip()
print(title)

# Setting the desired price threshold
BUY_PRICE = 26.97

# Checking if the current price is below the desired price threshold
if price < BUY_PRICE:
    # Constructing the email message
    message = f"{title} is now {price}"

    # Storing the URL of the product page
    url = "https://www.amazon.com/ORIFANTOU-Polyhedral-Dungeons-Dragons-Playing/dp/B0CJFMN9T2/ref=sr_1_45?crid=2OJADJRKVX267&dib=eyJ2IjoiMSJ9.7k0LCS3I-CD9FtO2YbWSco2o1DfPH5I5fmSBjxe0wyPHuN7HDhn4g7LO5IzzJJ76eZE9rYIIC8gTEDL0Uic3NSTl-2YJHxhj1eYXYA-IcikwCPkVxty6Dgjzd9kpcxpKAzkti5GxNKQVWyAelaLCDroRMnVnoF_8hlju4boR7mxMlSrVPSpwTnM6j2fWnN2H-Dc85J-fiGkgVLg6mpreD3MEsZ322iob7ttiDoMr4Q3-ieBwHzwo_A-iM4SITDHjq5NEMTPL4zLY7WcP27FELRtXnFmr7B2GIRXRX1Kd0J8.3V_OKJyL_a5csf1x3DM9-FOdAdu2y99wzMygNFJU_Pc&dib_tag=se&keywords=dungeons%2Band%2Bdragons%2Bdice&qid=1710495660&sprefix=dungeons%2B%2Caps%2C380&sr=8-45&th=1"

    # Setting up SMTP connection
    with smtplib.SMTP(YOUR_SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(YOUR_EMAIL, YOUR_PASSWORD)

        # Sending email notification
        connection.sendmail(
            from_addr=YOUR_EMAIL,
            to_addrs=YOUR_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
        )
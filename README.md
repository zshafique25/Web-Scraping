# Web Scraping Project

This project scrapes product information from a website using Selenium WebDriver. The goal is to extract details about products, including names, prices, links, images, ratings, descriptions, and additional attributes.

## Project Structure

- `xpaths.py`: Contains XPath expressions used to locate elements on the web pages.
- `selenium_utils.py`: Provides utility functions for setting up the Selenium WebDriver, navigating pages, and interacting with web elements.
- `scraper.py`: Implements the main scraping logic, including extracting product details, descriptions, and color variations.
- `data_processing.py`: Processes the scraped data, formats it, and prepares it for export.
- `main.py`: The entry point of the application. Sets up the browser, performs the search, scrapes the data, and stores it in a CSV file.

## Dependencies

- `selenium`: For web scraping.
- `webdriver-manager`: For managing ChromeDriver.
- `pandas`: For data processing and exporting to CSV.
- `json`: For parsing JSON data.

## Setup

1. **Install Dependencies**

   Install the required Python packages using pip:

   ```bash
   pip install selenium webdriver-manager pandas

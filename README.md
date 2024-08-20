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

2. **Setup WebDriver**

   Make sure you have Chrome installed. The `webdriver-manager` package will handle the installation of the ChromeDriver 
   automatically.

## Usage

1. **Run the Main Script**

   Execute the `main.py` script to start the scraping process:

   ```bash
   python main.py
   ```
   
   This will:
 - Set up the Selenium WebDriver.
 - Navigate to the specified URL and perform a search.
 - Scrape product details from the search results.
 - Process the data and save it to a CSV file named `products.csv`.

## Notes

- Adjust the `sleep` times if you encounter issues with page loading.
- Update XPath expressions in 'xpaths.py' if the website structure changes.
- Ensure that you comply with the website's terms of service and robots.txt file when scraping data.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

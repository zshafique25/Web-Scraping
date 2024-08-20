# main.py
from selenium_utils import setup_driver, navigate_to_url, send_keys_and_click
from xpaths import input_xpath, search_xpath
from scraper import scrape_products
from data_processing import process_data
from time import sleep
import csv

def store_data_to_csv(data, filename):
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['Name', 'Price', 'Link', 'Image_URL', 'Rating', 'Description', 'Product ID', 
                          'Manufactured By', 'Sold By', 'Width', 'Depth', 'Height', 'Weight', 'Color', 'Materials', 'Category', 
                          'Style', 'Number of Colors', 'List of Colors']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for row in data:
                writer.writerow(row)
    except Exception as e:
        print(f"Error storing data to CSV: {e}")

def main():
    url = 'https://www.houzz.com/products/'
    search_query = 'Sofas'
    
    browser = setup_driver()
    if browser is None:
        print("Failed to set up the browser.")
        return

    navigate_to_url(browser, url)
    print("Page source:", browser.page_source)
    send_keys_and_click(browser, input_xpath, search_xpath, search_query)
    sleep(5)  # give the page some time to load
    
    products = scrape_products(browser)
    print("Products:", products)
    df = process_data(products)
    print(df)

    # Store data to CSV file
    store_data_to_csv(df.to_dict('records'), 'products.csv')

if __name__ == '__main__':
    main()
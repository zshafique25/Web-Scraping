# scraper.py
from selenium_utils import setup_driver, navigate_to_url, find_elements, send_keys_and_click
from xpaths import name_xpath, price_xpath, link_xpath, image_xpath, rating_xpath, next_page_xpath, description_xpath, specification_xpath, product_id_xpath, manufactured_by_xpath, sold_by_xpath, size_weight_xpath, color_xpath, materials_xpath, category_xpath, style_xpath, color_variation_xpath, product_xpath
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import re
import json

def scrape_name(element):
    try:
        name_element = element.find_element(By.XPATH, name_xpath)
        return name_element.text.strip()
    except Exception as e:
        print(f"Error scraping name: {e}")
        return ""

def scrape_price(element):
    try:
        price_elements = element.find_elements(By.XPATH, price_xpath)
        return [price.text.strip() for price in price_elements]
    except Exception as e:
        print(f"Error scraping price: {e}")
        return []

def scrape_link(element):
    try:
        link_element = element.find_element(By.XPATH, link_xpath)
        return link_element.get_attribute('href')
    except Exception as e:
        print(f"Error scraping link: {e}")
        return ""

def scrape_image(element):
    try:
        image_element = element.find_element(By.XPATH, image_xpath)
        return image_element.get_attribute('src')
    except Exception as e:
        print(f"Error scraping image: {e}")
        return ""

def scrape_rating(element):
    try:
        rating_element = element.find_element(By.XPATH, rating_xpath)
        return rating_element.get_attribute('aria-label')
    except Exception as e:
        print(f"Error scraping rating: {e}")
        return ""
    
def scrape_description(browser):
    try:
        # Wait for the product page to load
        try:
            WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, description_xpath)))
        except Exception as e:
            print(f"Error waiting for product page to load: {e}")

        # Extract the product description
        description = browser.find_element(By.XPATH, description_xpath)
        return description.text.strip()
    except Exception as e:
        print(f"Error scraping product description: {e}")
        return ""
    
def scrape_product_details(browser):
    try:

        spec_tab = browser.find_element(By.XPATH, specification_xpath)
        spec_tab.click()
        sleep(10)  # Adjust sleep time as needed to ensure the tab content loads

        # Product ID
        product_id_element = browser.find_element(By.XPATH, product_id_xpath)
        product_id = product_id_element.text.strip()

        # Manufactured By
        try:
            manufactured_by_element = browser.find_element(By.XPATH, manufactured_by_xpath)
            manufactured_by = manufactured_by_element.text.strip()
        except:
            manufactured_by = ''

        # Sold By
        sold_by_element = browser.find_element(By.XPATH, sold_by_xpath)
        sold_by = sold_by_element.text.strip()

        # Size/Weight
        size_weight_element = browser.find_element(By.XPATH, size_weight_xpath)
        size_weight = size_weight_element.text.strip()
        # print("Size/Weight:", size_weight)

        # Size/Weight
        width = None
        depth = None
        height = None
        weight = None

        # Splitting the size_weight string based on specific substrings
        components = re.split(r'\s*(?:W|D|H|lb.)?\s*/\s*', size_weight)
        # print("Components:", components)

        for component in components:
            if 'W' in component:
                width_str = component.split()[1]  # Extract the numerical value
                width = float(width_str.replace('"', '')) if width_str else None  # Convert to float
            elif 'D' in component:
                depth_str = component.split()[1]
                depth = float(depth_str.replace('"', '')) if depth_str else None
            elif 'H' in component:
                height_str = component.split()[1]
                height = float(height_str.replace('"', '')) if height_str else None
            elif 'lb.' in component:
                weight_str = component.split()[0]
                weight = float(weight_str) if weight_str else None

        # print("Width:", width)
        # print("Depth:", depth)
        # print("Height:", height)
        # print("Weight:", weight)

        # Color (if available)
        try:
            color_element = browser.find_element(By.XPATH, color_xpath)
            color = color_element.text.strip()
        except:
            color = ''

        # Materials
        try:
            materials_element = browser.find_element(By.XPATH, materials_xpath)
            materials = materials_element.text.strip()
        except:
            materials = ''

        # Category
        category_element = browser.find_element(By.XPATH, category_xpath)
        category = category_element.text.strip()

        # Style
        style_element = browser.find_element(By.XPATH, style_xpath)
        style = style_element.text.strip()

        return {
            'Product ID': product_id,
            'Manufactured By': manufactured_by,
            'Sold By': sold_by,
            'Width': width,
            'Depth': depth,
            'Height': height,
            'Weight': weight,
            'Color': color,
            'Materials': materials,
            'Category': category,
            'Style': style
        }
    except Exception as e:
        print(f"Error scraping product details: {e}")
        return {
            'Product ID': '',
            'Manufactured By': '',
            'Sold By': '',
            'Width': '',
            'Depth': '',
            'Height': '',
            'Weight': '',
            'Color': '',
            'Materials': '',
            'Category': '',
            'Style': ''
        }
    
def scrape_color_variations(browser):
    try:
        color_info = {}

        # Find the div element containing color variation information
        color_div = browser.find_element(By.XPATH, color_variation_xpath)
        
        # Extract data-extra-info attribute containing JSON data
        extra_info_str = color_div.get_attribute('data-extra-info')

        # Parse JSON data
        extra_info = json.loads(extra_info_str)

        # Print the extracted extra_info dictionary for debugging
        # print("Extra Info:", extra_info)

        try:
            color_variation_info = extra_info['colorVariationExtraInfo']
            color_info['Number of Colors'] = color_variation_info.get('numberOfColors', 0)
            color_info['List of Colors'] = color_variation_info.get('listOfColors', [])
        except KeyError as e:
            color_info['Number of Colors'] = 0
            color_info['List of Colors'] = []

        return color_info
    except Exception as e:
        print(f"Error scraping color variations: {e}")
        return {}

def scrape_products(browser):
    try:
        products = []
        page_num = 1
        while True:
            print('Scraping page', page_num)
            print('Current URL:', browser.current_url)  # Debug output: Print current URL

            # Wait for product elements to be present
            try:
                WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located((By.XPATH, product_xpath)))
            except Exception as e:
                print(f"Error waiting for elements: {e}")

            html = browser.page_source
            print("HTML:", html)
            product_elements = browser.find_elements(By.XPATH, product_xpath)
            print("Product elements:", product_elements)

            for p in product_elements:
                try:
                    name = scrape_name(p)
                    prices = scrape_price(p)
                    link = scrape_link(p)
                    image_url = scrape_image(p)
                    rating = scrape_rating(p)
                    
                    # Open the product page to extract the description and additional details
                    browser.execute_script("window.open(arguments[0], '_blank');", link)
                    browser.switch_to.window(browser.window_handles[1])  # Switch to the newly opened tab
                    description = scrape_description(browser)
                    sleep(5)
                    product_details = scrape_product_details(browser)
                    sleep(5)
                    # Scrape color variations for each product
                    color_info = scrape_color_variations(browser)
                    # Update product dictionary with color information
                    product_details.update(color_info)
                    sleep(3)
                    browser.close()  # Close the product page tab
                    browser.switch_to.window(browser.window_handles[0])  # Switch back to the main page

                    products.append({'Name': name, 'Price': prices, 'Link': link, 'Image_URL': image_url, 'Rating': rating, 'Description': description, **product_details})
                except Exception as e:
                    print(f"Error scraping product data: {e}")

            try:
                next_button = browser.find_element(By.XPATH, next_page_xpath)
                next_button.click()
                # Wait for the page to load
                sleep(10)
                print('Navigated to Next Page')
                print('New URL:', browser.current_url)  # Debug output: Print new URL
                page_num += 1
            except Exception as e:
                print(f"Error navigating to next page: {e}")
                break

            sleep(10)

        return products
    except Exception as e:
        print(f"Error scraping products: {e}")
        return []
    
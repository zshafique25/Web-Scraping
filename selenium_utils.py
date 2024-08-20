# selenium_utils.py
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

def setup_driver():
    try:
        options = Options()
        # You can add other options here if needed
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        return driver
    except Exception as e:
        print(f"Error setting up driver: {e}")
        return None

def navigate_to_url(browser, url):
    try:
        browser.get(url)
        browser.maximize_window()
    except Exception as e:
        print(f"Error navigating to URL: {e}")

def find_elements(browser, xpath):
    try:
        return browser.find_elements(By.XPATH, xpath)
    except Exception as e:
        print(f"Error finding elements: {e}")
        return []

def send_keys_and_click(browser, input_xpath, search_button_xpath, search_query):
    try:
        input_search = browser.find_element(By.XPATH, input_xpath)
        search_button = browser.find_element(By.XPATH, search_button_xpath)
        input_search.send_keys(search_query)
        sleep(1)
        search_button.click()
    except Exception as e:
        print(f"Error sending keys and clicking: {e}")
        
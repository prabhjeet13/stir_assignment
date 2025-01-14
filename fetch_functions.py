from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
from pymongo import MongoClient
import os
import time
import uuid
import requests
from bs4 import BeautifulSoup
from bson import ObjectId
load_dotenv()

client = MongoClient(os.getenv("MONGODB_URL"))
db = client["twitter_trends"]
collection = db["trends"] 

def serialize_document(document):
    if '_id' in document:
        document['_id'] = str(document['_id'])  # Convert ObjectId to string

    return document


def get_save_trends():
    start_time = time.time()  # Start time for the script
    try:
        # Path to chromedriver
        chromedriver_path = os.getenv("CHROME_DRIVER_PATH")  # Update this to your chromedriver path
        # Set up Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        # Set up Chrome driver
        service = Service(chromedriver_path)
        driver = webdriver.Chrome(service=service, options=chrome_options)
        # Open the login page
        driver.get("https://x.com/i/flow/login")
        time.sleep(5)

        # Step 1: Enter username and click "Next"
        username_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='text']"))
        )
        username_field.send_keys(os.getenv('TWITTER_USERNAME'))
        username_field.send_keys(Keys.RETURN)
        time.sleep(5)

        # Step 2: Enter password and log in
        password_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='password']"))
        )
        password_field.send_keys(os.getenv('TWITTER_PASSWORD'))
        password_field.send_keys(Keys.RETURN)
        time.sleep(5)    

        # After login, navigate to the trending page
        driver.get("https://x.com/explore/tabs/trending")
        time.sleep(5)  # Random delay to mimic human behavior
        
        # Get the page source
        page_html = driver.page_source
        soup = BeautifulSoup(page_html, "html.parser")

        # Find all the divs that hold the trends
        trends = soup.find_all("div", {"data-testid": "trend"}, limit=5)

        # Collect the trend data
        trending_data = []
        for trend in trends:
            try:
                # Find the topic name inside the div
                topic_name = trend.find('div', class_='css-146c3p1 r-bcqeeo r-1ttztb7 r-qvutc0 r-37j5jr r-a023e6 r-rjixqe r-b88u0q r-1bymd8e')
                if topic_name:
                    # Get the text of the topic
                    trending_data.append(topic_name.get_text(strip=True))
            except Exception as e:
                print(f"Error parsing trend: {e}")
                continue

        try:
            ip_response = requests.get('https://api.ipify.org', timeout=5)
            ip_address = ip_response.text
        except Exception as ip_error:
            ip_address = "Could not fetch IP"
            print(f"Error fetching IP: {ip_error}")
        
        # Capture end time and elapsed time
        end_time = time.time()
        elapsed_time = end_time - start_time

        # Generate unique ID for the entry
        unique_id = str(uuid.uuid4())    

        trending_details = {
           "uinqueId" : unique_id,
           "trends" : trending_data,
           "start_time" : start_time,
           "end_time" :   end_time,  
           "ipaddress":   ip_address
        }         

        try:
            collection.insert_one(trending_details)
        except:
            print('error in saving db')    

        # Print the collected trends
        print(f"Trending topics: {trending_data}")
        print(f"Trending topics: {trending_details}")
        return serialize_document(trending_details)

    except Exception as e:
        print(f"Error: {e}")
    finally:
        driver.quit()


def fetch_from_db():    
    try:
        trending_documents = list(collection.find()) 
        serialized_documents = [serialize_document(doc) for doc in trending_documents]  
        return serialized_documents
    except Exception as e:
        print(f"Error : {e}")    

from flask import Flask, render_template,jsonify,request
from fetch_functions import get_save_trends, fetch_from_db
from flask import Response 
import json
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fetch-trends',methods=['GET'])
def fetch_trends():
    try:
        trending_data = get_save_trends()
        response_data = json.dumps({"success": True, "message": "data fetched successfully", "trend": trending_data}, ensure_ascii=False)
        return Response(response_data, mimetype='application/json; charset=utf-8'), 200
    except Exception as e:
        return jsonify({"error":str(e)}),500


@app.route('/get-trends',methods=["GET"])
def get_trends_from_db():
    try:
        trends = fetch_from_db()
        # Manually convert to JSON with UTF-8 encoding, ensure_ascii=False to keep Unicode intact
        response_data = json.dumps({"success": True, "message": "data fetched successfully", "trends": trends}, ensure_ascii=False)
        return Response(response_data, mimetype='application/json; charset=utf-8'), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)














# Iterate through each div element and find the corresponding span element inside it
    #     trends = []
    #     for span in div_elements:
    # # Check if the div matches the required class
    #     # Find the span inside this div with the required class
    #                 if "css-1jxf684.r-bcqeeo.r-1ttztb7.r-qvutc0.r-poiln3" in span.get_attribute("class"):    
    #             # span_element = div.find_element(By.CSS_SELECTOR, "span.css-1jxf684.r-bcqeeo.r-1ttztb7.r-qvutc0.r-poiln3")
    #     # Get the text of the span element and append it to the trends list
    #                     trends.append(span.text)

# Print the extracted trends
        # ip_response = requests.get('https://api.ipify.org')
        # ip_address = ip_response.text
        
        # # Capture end time and elapsed time
        # end_time = time.time()
        # elapsed_time = end_time - start_time

        # # Generate unique ID for the entry
        # unique_id = str(uuid.uuid4())

        # trend_data = {
        #     "uniqueID": unique_id,
        #     "trend1": trends[0] if len(trends) > 0 else None,
        #     "trend2": trends[1] if len(trends) > 1 else None,
        #     "trend3": trends[2] if len(trends) > 2 else None,
        #     "trend4": trends[3] if len(trends) > 3 else None,
        #     "trend5": trends[4] if len(trends) > 4 else None,
        #     "startTime": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(start_time)),
        #     "endTime": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(end_time)),
        #     "elapsedTime": elapsed_time,
        #     "date": time.strftime("%Y-%m-%d %H:%M:%S"),
        #     "ipAddress": ip_address,
        # }
        
        # Save to MongoDB
        # collection.insert_one(trend_data)
        


# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from pymongo import MongoClient
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from dotenv import load_dotenv
# import os
# import time
# import uuid
# import requests
# from datetime import datetime
# load_dotenv()

# PROXYMESH_URL = f"http://{os.getenv('USR_NAME')}:{os.getenv('PASS')}@proxy.proxy_mesh.com:31280"
# client = MongoClient(os.getenv("MONODB_URL"))
# db = client['twitter_trends']
# collection = db['trends']
# # Path to chromedriver
# chromedriver_path = os.getenv("CHROME_DRIVER_PATH")  # Update this to your chromedriver path
# # Set up Chrome options
# chrome_options = Options()
# chrome_options.add_argument("--start-maximized")
# chrome_options.add_argument(f"--proxy-server={PROXYMESH_URL}")
# # Set up Chrome driver
# service = Service(chromedriver_path)
# driver = webdriver.Chrome(service=service, options=chrome_options)



# def get_trends():
    
#     start_time = time.time()  # Start time for the script
    
#     try:
#         # Open a website
#         driver.get("https://x.com/i/flow/login")
#         time.sleep(5)
        
#         # Step 1: Enter username and click "Next"
#         username_field = WebDriverWait(driver, 20).until(
#             EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='text']"))
#         )
#         username_field.send_keys(os.getenv('TWITTER_USERNAME'))
#         username_field.send_keys(Keys.RETURN)
#         time.sleep(5)

#         password_field = WebDriverWait(driver, 20).until(
#             EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='password']"))
#         )
#         password_field.send_keys(os.getenv('TWITTER_PASSWORD'))
#         password_field.send_keys(Keys.RETURN)
#         time.sleep(5)

#         # Wait for homepage to load after login
#         WebDriverWait(driver, 30).until(
#             EC.presence_of_element_located((By.CSS_SELECTOR, "div[aria-label='Timeline: Trending now']"))
#         )
        
#         # Scrape top 5 trending topics
       
        
#         # Get the IP used by ProxyMesh
#         ip_response = requests.get('https://api.ipify.org')
#         ip_address = ip_response.text
        
#         # Capture end time and elapsed time
#         end_time = time.time()
#         elapsed_time = end_time - start_time

#         # Generate unique ID for the entry
#         unique_id = str(uuid.uuid4())

#         trend_data = {
#             "uniqueID": unique_id,
#             "trend1": trends[0],
#             "trend2": trends[1],
#             "trend3": trends[2],
#             "trend4": trends[3],
#             "trend5": trends[4],
#             "startTime": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(start_time)),
#             "endTime": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(end_time)),
#             "elapsedTime": elapsed_time,
#             "date": time.strftime("%Y-%m-%d %H:%M:%S"),
#             "ipAddress": ip_address,
#         }
        
#         # Save to MongoDB
#         collection.insert_one(trend_data)
        
#         print(f"Trends saved: {trends}")

#     except Exception as e:
#         print(f"Error: {e}")
#     finally:
#         driver.quit()

# if __name__ == "__main__":
#     get_trends()
# # # Close the browser after a delay
# # input("Press Enter to quit...")
# # driver.quit()
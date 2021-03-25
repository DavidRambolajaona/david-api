from flask import Blueprint, render_template, session, request, redirect, jsonify
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import time
import os

geolocation_bp = Blueprint('geolocation_bp', __name__, template_folder='template', static_folder='static', static_url_path='/geolocation-static')

@geolocation_bp.route('/geolocation/api/location')
def getLocationApi() :
    driver = getDriver()
    timeout = 20
    driver.get("https://mycurrentlocation.net/")
    wait = WebDriverWait(driver, timeout)
    time.sleep(3)
    longitude = driver.find_elements_by_xpath('//*[@id="longitude"]') #Replace with any XPath    
    longitude = [x.text for x in longitude]    
    longitude = str(longitude[0])    
    latitude = driver.find_elements_by_xpath('//*[@id="latitude"]')    
    latitude = [x.text for x in latitude]    
    latitude = str(latitude[0])    
    driver.quit()    
    return jsonify({"geocoding": {"longitude": longitude, "latitude": latitude}})

def getDriver():
    options = Options()
    options.add_argument("--use--fake-ui-for-media-stream")
    dir_path = os.path.dirname(os.path.realpath(__file__)).replace("\\", "/")
    driver = webdriver.Chrome(executable_path = dir_path + "/chromedriver.exe",options=options)
    return driver
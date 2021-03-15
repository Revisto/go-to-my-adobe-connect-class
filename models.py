from dotenv import load_dotenv
from os import getenv

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
 

class SeleniumAutomation:
    def __init__(self):
        load_dotenv()
        self.adobe_connect_class_url = getenv("adobe_connect_class_url")
        self.adobe_connect_username = getenv("adobe_connect_username")
        self.adobe_connect_password = getenv("adobe_connect_password")
        self.chrome_webdriver_path = getenv("chrome_webdriver_path")
    
    def setup_selenium_drive(self):
        self.driver = webdriver.Chrome(self.chrome_webdriver_path)
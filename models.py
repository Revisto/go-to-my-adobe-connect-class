from dotenv import load_dotenv
from os import getenv

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from validator_collection import *
from time import sleep
class SeleniumAutomation:
    def __init__(self):
        load_dotenv()
        self.adobe_connect_class_url = getenv("adobe_connect_class_url")
        self.adobe_connect_username = getenv("adobe_connect_username")
        self.adobe_connect_password = getenv("adobe_connect_password")
        self.chrome_webdriver_path = getenv("chrome_webdriver_path")
        self.delay_time = 3
    
    def delay(self, delay_time = None):
        if is_none(delay_time):
            delay_time = self.delay_time
        sleep(self.delay_time)

    def setup_selenium_drive_with_android_useragent(self):
        options = Options()
        options.add_argument("--headless")  
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument("user-agent=Mozilla/5.0 (Linux; Android 6.0; HTC One M9 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36")
        self.driver = webdriver.Chrome(executable_path=self.chrome_webdriver_path, chrome_options=options)

    def go_to_my_adobe_connect_class_url(self):
        self.driver.get(self.adobe_connect_class_url)
        SeleniumAutomation().delay()

    def log_in_into_adobe_connect_class(self):
        self.driver.find_element_by_name("login").send_keys(self.adobe_connect_username)
        self.driver.find_element_by_name("password").send_keys(self.adobe_connect_password)
        self.driver.find_element_by_xpath("//input[@type='submit']").click()
        SeleniumAutomation().delay()
        self.driver.find_elements_by_class_name("open-in-browser-button")[-1].click()
        
    def type_something_in_chatbar(self, text):
        self.driver.find_elements_by_class_name("spectrum-Button")[1].click() 
        textarea = self.driver.find_element_by_css_selector("textarea")
        textarea.send_keys(text)
        textarea.send_keys(Keys.RETURN)
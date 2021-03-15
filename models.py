from dotenv import load_dotenv
from os import getenv


class SeleniumAutomation:
    def __init__(self):
        load_dotenv()
        self.adobe_connect_class_url = getenv("adobe_connect_class_url")
        self.adobe_connect_username = getenv("adobe_connect_username")
        self.adobe_connect_password = getenv("adobe_connect_password")
        self.chrome_webdriver_path = getenv("chrome_webdriver_path")
    

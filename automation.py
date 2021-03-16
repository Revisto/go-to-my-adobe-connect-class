from models import *

SA = SeleniumAutomation()
SA.setup_selenium_drive_with_android_useragent()
SA.go_to_my_adobe_connect_class_url()
SA.log_in_into_adobe_connect_class()
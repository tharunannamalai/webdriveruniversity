"""
This file contains the class object for file upload page.
"""
#--------------------------------------------------------
#   IMPORTS
#--------------------------------------------------------

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert

class FileUpload:
    #INITIALIZERS
    def __init__(self,browser):
        self.browser = browser

    #LOCATORS
    FILE_UPLOAD = (By.XPATH,"//input[@type = 'file']")
    SUBMIT_BUTTON = (By.ID,"submit-button")
    #URL   
    URL = "http://www.webdriveruniversity.com/File-Upload/index.html?filename=Api+Learning.txt"  
    
    def loadpage(self):
        self.browser.get(self.URL)
    
    def uploadfile(self,filepath):
        file_upload = self.browser.find_element(*self.FILE_UPLOAD)
        file_upload.send_keys(filepath)

        submit_button = self.browser.find_element(*self.SUBMIT_BUTTON)
        submit_button.click()
        
        alert = Alert(self.browser)
        alerttext = alert.text
        alert.accept()
        
        return alerttext



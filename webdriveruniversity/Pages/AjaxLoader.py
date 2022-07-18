"""
   This File contains the class object for the ajax page
"""

#----------------------------------------------------------
#   IMPORTS
#----------------------------------------------------------

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AjaxLoader():

    #INTIALIZERS
    def __init__(self,browser):
      self.browser = browser
    
    #URL
    URL = "http://www.webdriveruniversity.com/Ajax-Loader/index.html"
    
    #LOCATORS
    CLICKMEBUTTON = (By.ID,"button1")
    ALERTBOXTEXT = (By.TAG_NAME,"h4")
    CLOSEBUTTON = (By.XPATH,"//button[@class = 'close']")

    def loadpage(self):
        self.browser.get(self.URL)    
    
    def clickajaxbutton(self):

        ajaxbutton = self.browser.find_element(*self.CLICKMEBUTTON)
        WebDriverWait(self.browser,10).until(EC.visibility_of_element_located(self.CLICKMEBUTTON))
        WebDriverWait(self.browser,10).until(EC.element_to_be_clickable(self.CLICKMEBUTTON))
        ajaxbutton.click()

        alerttext = self.browser.find_element(*self.ALERTBOXTEXT)
        time.sleep(5)
        textone = alerttext.text
        

        closebutton = self.browser.find_element(*self.CLOSEBUTTON)
        closebutton.click()

        return textone

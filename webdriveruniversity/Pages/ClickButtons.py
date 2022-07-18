'''
    This Class Is the page object for button click page
'''

#---------------------------------------------------------------
#     IMPORT
#---------------------------------------------------------------

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ClickButtons:

    #URL
    URL = "http://www.webdriveruniversity.com/Click-Buttons/index.html"

    #LOCATORS
    WEBELEMENTBUTTON = (By.ID,'button1')
    WEBELEMENTBUTTONTEXT = (By.XPATH,"//h4[contains(text(),'Congratulations!')]")
    CLOSEBUTTON2 = (By.XPATH,"//button[@class = 'btn btn-default']")
    CLOSEBUTTON = (By.CSS_SELECTOR,'.close')
    JAVASCRIPTBUTTON = (By.CSS_SELECTOR,"#button2")
    JAVASCRIPTBUTTONTEXT = (By.XPATH,"//h4[contains(text(),'It’s that Easy!!  Well I think it is.....')]")
    ACTIONBUTTON = (By.ID,'button3')
    ACTIONBUTTONTEXT = (By.XPATH,"//h4[contains(text(),'Well done! the')]")
    
    #INTIALIZERS
    def __init__(self, browser):
        self.browser = browser 

    def loadpage(self):
        self.browser.get(self.URL)    
    
    def clickthreediffbuttons(self):
        
        
        #BUTTON 1
        button1 = self.browser.find_element(*self.WEBELEMENTBUTTON)
        button1.click()
        time.sleep(10)
        buttontextone = self.browser.find_element(*self.WEBELEMENTBUTTONTEXT)
        textone = buttontextone.text
        WebDriverWait(self.browser,10).until(EC.element_to_be_clickable(self.CLOSEBUTTON))
        closebutton = self.browser.find_element(*self.CLOSEBUTTON)
        closebutton.click()
        
        """
        #BUTTON 2
        WebDriverWait(self.browser,10).until(EC.element_to_be_clickable(self.JAVASCRIPTBUTTON))
        button2 = self.browser.find_element(*self.JAVASCRIPTBUTTON)
        self.browser.execute_script("arguments[0].click()",button2)
        time.sleep(10)
        buttontexttwo = self.browser.find_element(*self.JAVASCRIPTBUTTONTEXT)
        texttwo = buttontexttwo.text
        closebutton = self.browser.find_element(*self.CLOSEBUTTON)
        self.browser.execute_script("arguments[0].click();",closebutton)
        """

        #BUTTON 3
        
        button3 = self.browser.find_element(*self.ACTIONBUTTON)
        button3.click()
        time.sleep(10)
        buttontextthree = self.browser.find_element(*self.ACTIONBUTTONTEXT)
        textthree = buttontextthree.text
        closebutton = self.browser.find_element(*self.CLOSEBUTTON)
        self.browser.execute_script("arguments[0].click();",closebutton)
        
        return textone,textthree

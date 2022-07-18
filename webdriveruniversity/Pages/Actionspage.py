"""
 This file contains the class object for actions page.
"""

#----------------------------------------------------------
#  IMPORTS
#----------------------------------------------------------

import time
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.color import Color
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class Actionpage:

    #INTIALIZER
    def __init__(self,browser):
        self.browser = browser

    #URL
    URL = "http://www.webdriveruniversity.com/Actions/index.html#"    

    #LOCATORS
    SOURCEDROP = (By.CSS_SELECTOR,"#draggable")
    TARGETDROP = (By.CSS_SELECTOR,"#droppable")
    DROPPEDTEXT = (By.XPATH,"//b[contains(text(),'Dropped!')]")
    DOUBLECLICKBUTTON = (By.ID,"double-click")
    HOVERBUTTONTHREE = (By.XPATH,"//div[@id = 'div-hover']/div[3]")
    DROPDOWNLINK = (By.XPATH,"//div[@class = 'dropdown-content']/a[2]")
    CLICKHOLDBUTTON = (By.ID,"click-box")

    def loadpage(self):
        self.browser.get(self.URL)
    
    
    def actionmoving(self):
         source = self.browser.find_element(*self.SOURCEDROP)
         target = self.browser.find_element(*self.TARGETDROP)
         
         action = ActionChains(self.browser,duration=700)
         action.drag_and_drop(source,target)
         action.perform()

         droppedtext = self.browser.find_element(*self.DROPPEDTEXT)
         time.sleep(2)
         textone = droppedtext.text

         return textone
        

    def doubleclickbutton(self):
        dclickbutton = self.browser.find_element(*self.DOUBLECLICKBUTTON)

        action = ActionChains(self.browser,duration=500)
        action.double_click(dclickbutton)
        action.perform()
        
        bgcolorchange = dclickbutton.value_of_css_property("background-color")
        hexvalue = Color.from_string(bgcolorchange).hex

        return hexvalue

    def mousehover(self):
         mousebutton = self.browser.find_element(*self.HOVERBUTTONTHREE)

         action = ActionChains(self.browser,duration=500)
         action.move_to_element(mousebutton)
         action.perform()

         link = self.browser.find_element(*self.DROPDOWNLINK)
         link.click()

         alert = Alert(self.browser)
         time.sleep(5)
         alerttext = alert.text
         alert.accept()

         return alerttext

"""
    def clickandhold(self):
        clickhold = self.browser.find_element(*self.CLICKHOLDBUTTON)

        self.browser.execute_script("window.scrollBy(0,1000)")
        time.sleep(5)
        action = ActionChains(self.browser,duration=100)
        action.move_to_element(clickhold)
        action.click_and_hold(clickhold)
        time.sleep(10)
        action.perform
        bgcolorclickhold = clickhold.value_of_css_property("background-color")
        hexvalue = Color.from_string(bgcolorclickhold).hex

        return hexvalue

"""

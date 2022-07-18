"""
  This file contains the page object for the dropdown,checkbox,radiobuttons
"""

#----------------------------------------------
#    IMPORTS
#----------------------------------------------

import time
from selenium.webdriver.common.by import By

class DropdownCheckRadio:

    #INTIALIZERS
    def __init__(self,browser):
        self.browser = browser

    #LOCATORS
    DROPDOWN1 = (By.ID,'dropdowm-menu-1')
    DROPDOWN1OPTION = (By.XPATH,"//select[@id = 'dropdowm-menu-1']/option[4]")
    DROPDOWN2 = (By.ID,'dropdowm-menu-2')
    DROPDOWN2OPTION = (By.XPATH,"//select[@id = 'dropdowm-menu-2']/option[4]")
    DROPDOWN3 = (By.ID,'dropdowm-menu-3')
    DROPDOWN3OPTION = (By.XPATH,"//select[@id = 'dropdowm-menu-3']/option[4]")
    CHECKBOX1 = (By.XPATH,"//input[@value='option-1']")
    CHECKBOX2 = (By.XPATH,"//input[@value='option-2']")
    CHECKBOX3 = (By.XPATH,"//input[@value='option-3']")
    CHECKBOX4 = (By.XPATH,"//input[@value='option-4']")
    RADIOBUTTON1 = (By.XPATH,"//input[@type = 'radio' ][@value = 'yellow']")
    

    #URL
    URL = 'http://www.webdriveruniversity.com/Dropdown-Checkboxes-RadioButtons/index.html'

    def loadpage(self):
        self.browser.get(self.URL)
  
    def dropdowns(self):
        dropdown1 = self.browser.find_element(*self.DROPDOWN1)
        dropdown1.click()
        dropdown1option = self.browser.find_element(*self.DROPDOWN1OPTION)
        dropdown1option.click()
        textone = dropdown1option.text

        dropdown2 = self.browser.find_element(*self.DROPDOWN2)
        dropdown2.click()
        dropdown2option = self.browser.find_element(*self.DROPDOWN2OPTION)
        dropdown2option.click()
        texttwo = dropdown2option.text

        dropdown3 = self.browser.find_element(*self.DROPDOWN3)
        dropdown3.click()
        dropdown3option = self.browser.find_element(*self.DROPDOWN3OPTION)
        dropdown3option.click()
        textthree = dropdown3option.text

        return textone,texttwo,textthree

    def checkboxes(self):

        checkbox1 = self.browser.find_element(*self.CHECKBOX1)
        if checkbox1.is_selected():
          box1 = checkbox1.is_selected()
        else:
          checkbox1.click()    
          box1 = checkbox1.is_selected()

        checkbox2 = self.browser.find_element(*self.CHECKBOX2)
        if checkbox2.is_selected():
          box2 = checkbox2.is_selected()  
        else:  
          checkbox2.click()  
          box2 = checkbox2.is_selected()

        checkbox3 = self.browser.find_element(*self.CHECKBOX3)
        if checkbox3.is_selected():
            box3 = checkbox3.is_selected()
        else:
            checkbox3.click()
            box3 = checkbox3.is_selected()    

        checkbox4 = self.browser.find_element(*self.CHECKBOX4)
        if checkbox4.is_selected():
            box4 = checkbox4.is_selected()
        else:
            checkbox4.click()
            box4 = checkbox4.is_selected()   

        return box1,box2,box3,box4

    def radiobuttons(self):    
         
         radiobutton = self.browser.find_element(*self.RADIOBUTTON1)

         if radiobutton.is_selected():
             selected = radiobutton.is_selected()
         else:
             radiobutton.click()
             selected = radiobutton.is_selected()
        
         return selected         



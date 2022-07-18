"""
     This File Contains the class page object for accordian page.
"""

#------------------------------------------------------------
#   IMPORT
#------------------------------------------------------------

from selenium.webdriver.common.by import By
import time

class Accordian:

    #INTIALIZERS
    def __init__(self,browser):
        self.browser = browser

    #URL
    URL = "http://www.webdriveruniversity.com/Accordion/index.html"

    #LOCATORS
    MANUALTESTINGCLICK = (By.ID,'manual-testing-accordion')
    MANUALTESTINGTEXT = (By.XPATH,"//div[@id = 'manual-testing-description']/p")
    CUCUMBERTESTING = (By.ID,'cucumber-accordion')
    CUCUMBERTESTINGTEXT = (By.XPATH,"//div[@id = 'cucumber-testing-description']/p")
    AUTOMATIONTESTING = (By.ID,'automation-accordion')
    AUTOMATIONTESTINGTEXT = (By.XPATH,"//div[@id = 'automation-testing-description']/p") 
    FIVESECACCORDIAN = (By.ID,'click-accordion')
    FIVESECACCORDIANTEXT = (By.XPATH,"//div[@id = 'timeout']")

    def loadpage(self):
        self.browser.get(self.URL)

    def ClickAccordians(self):
        #accordian 1
        manualtesting = self.browser.find_element(*self.MANUALTESTINGCLICK)
        manualtesting.click()
        manualtestingtext = self.browser.find_element(*self.MANUALTESTINGTEXT)
        textone = manualtestingtext.text
        time.sleep(2)
        manualtesting.click()
        

        #accordian 2
        cucumbertesting = self.browser.find_element(*self.CUCUMBERTESTING)
        cucumbertesting.click()
        cucumbertestingtext = self.browser.find_element(*self.CUCUMBERTESTINGTEXT)
        texttwo = cucumbertestingtext.text
        time.sleep(2)
        cucumbertesting.click()
       

        #accordian 3
        automationtesting = self.browser.find_element(*self.AUTOMATIONTESTING)
        automationtesting.click()
        automationtestingtext = self.browser.find_element(*self.AUTOMATIONTESTINGTEXT)
        textthree = automationtestingtext.text
        time.sleep(2)
        automationtesting.click()
        

        #accordian 4
        fivesecaccordian = self.browser.find_element(*self.FIVESECACCORDIAN)
        fivesecaccordian.click()
        fivesecaccordiantext = self.browser.find_element(*self.FIVESECACCORDIANTEXT)
        textfour = fivesecaccordiantext.text
        time.sleep(2)
        fivesecaccordian.click()

        return textone,texttwo,textthree,textfour











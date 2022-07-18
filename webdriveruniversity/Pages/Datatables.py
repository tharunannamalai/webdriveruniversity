"""
This File contains the page object for the webtable page 
"""
#----------------------------------------------------------
#  IMPORTS
#----------------------------------------------------------

from optparse import check_choice
import time
import pdb
from selenium.webdriver.common.by import By

class Webtablepage:
    
    #INTIALIZERS
    def __init__(self,browser):
        self.browser = browser

    #LOCATORS
    COLUMNS = (By.XPATH,"//table[@id = 't01']/tbody/tr/th")
    #URL    
    URL = "http://www.webdriveruniversity.com/Data-Table/index.html"

    def loadpage(self):
        self.browser.get(self.URL) 

    def get_column_info(self):
        columns =  self.browser.find_elements(*self.COLUMNS)
        for column in columns:
            print(column.text,end=" ") 
        print()    

    def get_tableresults(self,checkdata):
        self.get_column_info() 
        datapresent = False
        noofrows    = len(self.browser.find_elements_by_xpath("//table[@id = 't01']/tbody/tr"))
        noofcolumns = len(self.browser.find_elements_by_xpath("//table[@id = 't01']/tbody/tr[2]/td"))
        for tablerow in range(2,noofrows+1):
            for tablecolumn in range(1,noofcolumns+1):
                cool = self.browser.find_element_by_xpath("//table[@id = 't01']/tbody/tr["+str(tablerow)+"]/td["+str(tablecolumn)+"]").text
                if cool == checkdata:
                    datapresent = True

        return datapresent   
        
           

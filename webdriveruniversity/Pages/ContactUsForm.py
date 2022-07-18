'''
  This Class Is the page object for contactusform click page
'''
#---------------------------------------------------
# IMPORTS
#---------------------------------------------------

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class ContactUsForm:
  #URL
  URL = 'http://www.webdriveruniversity.com/Contact-Us/contactus.html'

  #Locators
  FIRSTNAME = (By.NAME, 'first_name')
  LASTNAME = (By.NAME, 'last_name')
  EMAIL = (By.NAME, 'email')
  COMMENT = (By.NAME, 'message')
  SUBMITBUTTON = (By.XPATH, "//div[@id = 'form_buttons']/input[2]")
  THANKYOUTEXT = (By.TAG_NAME, "h1")

  #Intializers
  def __init__(self, browser):
      self.browser = browser

  def loadpage(self):
      self.browser.get(self.URL)
      
  def filloutinfo(self,fname,lname,email,comment):
       
       WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(self.FIRSTNAME))
       fnelement = self.browser.find_element(*self.FIRSTNAME)
       fnelement.send_keys(fname)
       
       WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(self.LASTNAME))
       lnelement = self.browser.find_element(*self.LASTNAME)
       lnelement.send_keys(lname)
       
       WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(self.EMAIL))
       emailelement = self.browser.find_element(*self.EMAIL)
       emailelement.send_keys(email)

       comm = WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.COMMENT))
       print(comm)
       commentelement = self.browser.find_element(*self.COMMENT)
       commentelement.send_keys(comment)
            
  def clicksubmitbutton(self):
       WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.SUBMITBUTTON))
       submitelement = self.browser.find_element(*self.SUBMITBUTTON)    
       submitelement.click()   

  def thankyoudisplay(self):
       WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.THANKYOUTEXT))
       thanyout = self.browser.find_element(*self.THANKYOUTEXT)
       thankyoutext = thanyout.text
       print(thankyoutext)
       return thankyoutext
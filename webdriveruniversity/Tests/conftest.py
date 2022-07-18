'''
 This File Contains the common fixtures.
'''

#-----------------------------------------------------
# IMPORT
#-----------------------------------------------------

import pytest
import selenium.webdriver

@pytest.fixture()
def browser():
   #initialize the chrome instance
 driver = selenium.webdriver.Chrome()
   #Maximizing the window
 driver.maximize_window()  
   #Making the Driver wait for 10 seconds to load elements
 driver.implicitly_wait(30)
   #Return the webdriver instances for the setup
 yield driver

   #Quit the webdriver instances for the cleanup
 driver.quit()




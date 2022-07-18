'''
 This Test class will test the data added to the tables.
'''

#------------------------------------------
#  IMPORT
#------------------------------------------

import pytest
from Pages.ContactUsForm import ContactUsForm
from assertpy import assert_that

@pytest.mark.contactuspage
def test_webtablepage(browser):
  contactus_form =  ContactUsForm(browser)
  fname, lname, email, comment = "tharun", "annamalai", "tgt@gmail.com", "tharun is a good boy."
   
  #Given the webdriveruniversity's contactusfrom page
  contactus_form.loadpage()
  #When Entered all the information
  contactus_form.filloutinfo(fname,lname,email,comment)
  #And Clicked Submit button
  contactus_form.clicksubmitbutton()
  #Then Thank You Should displayed.
  valuetext = contactus_form.THANKYOUTEXT
  print(valuetext)
  #assert_that(valuetext,"thankyou text is not equal to value").is_equal_to('Thank You for your Message!')
  

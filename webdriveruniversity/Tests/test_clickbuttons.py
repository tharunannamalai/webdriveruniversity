"""
   This File Contains the test method to test action buttons
"""
#-----------------------------------------------------------
#   IMPORT
#-----------------------------------------------------------

import pytest
from assertpy import assert_that
from Pages.ClickButtons import ClickButtons

@pytest.mark.clickbuttons
def test_clickbuttons(browser):
   click_button = ClickButtons(browser)

  # Given the clickbutton page    
   click_button.loadpage()
  # When Clicking All the button
   returntext = click_button.clickthreediffbuttons()
  # Then the alert message should show
   assert_that(returntext[0]).is_equal_to("Congratulations!")
   #assert_that(returntext[1]).is_equal_to("It’s that Easy!!  Well I think it is.....")
   assert_that(returntext[1]).is_equal_to("Well done! the Action Move & Click can become very useful!")
  
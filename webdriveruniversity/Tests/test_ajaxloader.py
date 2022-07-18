"""
   This File contains the test method for ajaxloader page
"""

#--------------------------------------------------------
#   IMPORTS
#--------------------------------------------------------
import pytest
from Pages.AjaxLoader import AjaxLoader
from assertpy import assert_that

@pytest.mark.ajaxloader
def test_ajaxloader(browser):

    ajaxloader = AjaxLoader(browser)
    #Given the website the Alaxloader page
    ajaxloader.loadpage()
    #When the ajaxloader finished loading and cliked the click me button
    #returntext = ajaxloader.clickajaxbutton()
    #Then the alert should open and show message
    assert_that(ajaxloader.clickajaxbutton()).is_equal_to("Well Done For Waiting....!!!")
 
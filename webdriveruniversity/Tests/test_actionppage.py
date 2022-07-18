"""
   This file contains the test method to action page in the website
"""

#------------------------------------------------------
#   IMPORTS
#------------------------------------------------------

import pytest
from Pages.Actionspage import Actionpage
from assertpy import assert_that

@pytest.mark.draganddrop
def test_actionpagemoving(browser):
    #DRAG AND DROP
    action_page = Actionpage(browser)
    #Given the drag n drop section page of the website
    action_page.loadpage()
    #When the drag n dropped element to target place
    returntext = action_page.actionmoving()
    #Then the target should change 
    assert_that(returntext).is_equal_to("Dropped!")

@pytest.mark.doubleclick
def test_doubleclick(browser):
   #DOUBLE CLICK SECTION
   doubleclick = Actionpage(browser)
   #Given the doubleclick section in the website
   doubleclick.loadpage()
   #When double clicking the button
   returnvalue = doubleclick.doubleclickbutton()
   #Then the colour of the button should change.
   assert_that(returnvalue).is_equal_to("#93cb5a")

@pytest.mark.hoverclick
def test_hoverclick(browser):
   #HOVER CLICK
   hoverclick = Actionpage(browser)
   #Given the HoverButton in the website
   hoverclick.loadpage()
   #When Hovering the third button And Clicking the Link
   returntext = hoverclick.mousehover()
   #Then the link should open an alert msg
   assert_that(returntext).is_equal_to("Well done you clicked on the link!")

"""
@pytest.mark.clickandhold
def test_clickandhold(browser):
   #CLICKHOLD SECTION
   click_hold = Actionpage(browser)
   #Given the clickandhold section in the website
   click_hold.loadpage()
   #When the button is clickandhold
   returntext = click_hold.clickandhold()
   #Then it should change and give msg
   assert_that(returntext).is_equal_to("#000000")
"""
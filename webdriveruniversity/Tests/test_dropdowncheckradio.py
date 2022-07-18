"""
  This file contains the test method to test deopdown,check,radio buttons page.
"""

#---------------------------------------------------
# IMPORTS
#---------------------------------------------------

import pytest
from Pages.DropdownCheckRadioButtons import DropdownCheckRadio
from assertpy import assert_that

@pytest.mark.dropdown
def test_dropdownsection(browser):
    
    #DROPDOWN SECTION
    dropdowncheck = DropdownCheckRadio(browser)

    #Given the dropdown section in the website
    dropdowncheck.loadpage()
    #When user chooses any of the options from the dropdowns
    returntext = dropdowncheck.dropdowns()
    #Then it should be selected.
    assert_that(returntext[0]).is_equal_to('SQL')
    assert_that(returntext[1]).is_equal_to('JUnit')
    assert_that(returntext[2]).is_equal_to('JQuery')

@pytest.mark.checkbox
def test_checkboxsection(browser):

    #CHECKBOX SECTION
    checkbox = DropdownCheckRadio(browser)

    #Given the checkbox section in the website
    checkbox.loadpage()
    #When user clicks the checkboxs
    selectedboxes = checkbox.checkboxes()
    #Then it should be selected.
    assert_that(selectedboxes[0]).is_true
    assert_that(selectedboxes[1]).is_true
    assert_that(selectedboxes[2]).is_true
    assert_that(selectedboxes[3]).is_true    

@pytest.mark.radio
def test_radiobuttonsection(browser):
    #DROPDOWN SECTION
    radio = DropdownCheckRadio(browser)

    #Given the radiobutton section in the website
    radio.loadpage()
    #When clicking the any radiobutton
    returnstatus = radio.radiobuttons()
    #Then the clicked button should be selected.
    assert_that(returnstatus).is_true
   


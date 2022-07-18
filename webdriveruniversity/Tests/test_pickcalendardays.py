"""
This file contains the test method to test calendar date
"""
#--------------------------------------------------------
#   IMPORTS
#--------------------------------------------------------

import pytest
from assertpy import assert_that
from Pages.Datepicker import DatePicker

@pytest.mark.calendardate
def test_pickcalendar(browser):

    date_picker = DatePicker(browser)
    date = "12-19-1999"

    #Given the calendar section in the website
    date_picker.loadpage()
    #When target date gets selected in the calendar
    returntext = date_picker.pickcalendardate(date)
    #then the date the text need to change to selected date.
    assert_that(returntext).is_equal_to(date)
"""
This file contians the test method to the datatables pages 
"""
#---------------------------------------------------------
#  IMPORTS
#---------------------------------------------------------

import pytest
from Pages.Datatables import Webtablepage
from assertpy import assert_that

@pytest.mark.datatable
def test_webtablepage(browser):

    web_table = Webtablepage(browser)
    testdata = "20"
    #Given the webtable in the website
    web_table.loadpage()
    #When got all the data
    returnindicate = web_table.get_tableresults(testdata)
    #Then it should print all
    assert_that(returnindicate).is_equal_to(True)

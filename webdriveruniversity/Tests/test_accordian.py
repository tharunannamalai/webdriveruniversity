"""
    This File Contains the test method to test action buttons
"""
#-----------------------------------------------------------
#  IMPORT
#-----------------------------------------------------------

import pytest
from assertpy import assert_that
from Pages.Accordian import Accordian

@pytest.mark.accordian
def test_accordians(browser):
    
    #INTIALIZERS
    testaccordian  = Accordian(browser)

    #Given the website accordian page
    testaccordian.loadpage()
    #when the all the accordians clicked
    returntext = testaccordian.ClickAccordians()
    #Then the accordians should open and expose the message.
    assert_that(returntext[0]).is_equal_to('Manual testing has for some time been the most popular way to test code. For this method, the tester plays an important role of end user and verifies that all the features of the application work correctly. Manual testing however is on the decline. Companies and developers have realised the efficiency, accuracy and cost savings that is possible by adopting the use of automation testing.')
    assert_that(returntext[1]).is_equal_to('Cucumber (BDD) simplifies the requirement capturing process. Requirements can be captured, broken down and simplified effortlessly; making the captured requirements readable to anyone within the organisation and in turn providing the required details and backbone to develop accurate test cases also known as ‘Feature Files’.')
    assert_that(returntext[2]).is_equal_to('Automation testing has been steadily grown in popularity these past few years thanks to the time/ cost savings and efficiency that it offers. Companies throughout the world have or plan to use automation testing to rapidly speed up their test capabilities. Automation test engineers are in great demand and offer an average salary of £45,000+ (2018). Now is a great time to learn about automation test engineering and this course has been carefully developed to slowly introduce you from the basics, all the way to building advanced frameworks.')
    assert_that(returntext[3]).is_equal_to('This text has appeared after 5 seconds!')
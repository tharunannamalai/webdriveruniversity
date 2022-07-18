"""
This file contains the test methods to test file upload page
"""
#---------------------------------------------------------
#  IMPORTS
#---------------------------------------------------------

import pytest
from assertpy import assert_that
from Pages.FileUpload import FileUpload

@pytest.mark.fileupload
def test_fileupload(browser):

    file_upload = FileUpload(browser)
    PATH_TO_FILE = "C:\\Users\\parthiban\\SeleniumIDE\\data.csv"
    #Given the file upload section in website
    file_upload.loadpage()
    #When the file has been uploaded and clicked submit
    returntext = file_upload.uploadfile(PATH_TO_FILE)
    #Then upload successfull alert should open
    assert_that(returntext).is_equal_to("Your file has now been uploaded!")

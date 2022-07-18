"""
This file contains the class for the date picker page
"""
#--------------------------------------------------
#  IMPORTS
#--------------------------------------------------

import pdb
import time
from selenium.webdriver.common.by import By

class DatePicker:
    #INTIALIZER
    def __init__(self,browser):
        self.browser = browser

    #LOCATORS
    CALENDAR_OPEN_BUTTON = (By.XPATH,"//i[@class = 'glyphicon glyphicon-calendar']")
    MONTH_DISPLAY_SECTION = (By.XPATH,"//table[@class = ' table-condensed']/thead/tr[1]/th[2]")
    SELECTED_CAL_YEAR = (By.XPATH,"//div[@class = 'datepicker-months']/table/thead[1]/tr[1]/th[2]")
    PREVIOUS_BUTTON = (By.XPATH,"//div[@class = 'datepicker-months']/table/thead[1]/tr[1]/th[1]")
    NEXT_BUTTON = (By.XPATH,"//div[@class = 'datepicker-months']/table/thead[1]/tr[1]/th[3]")
    CALENDAR_MONTHS = (By.XPATH,"//tbody/tr/td/span[@class = 'month']")
    CALENDAR_DAYS = (By.XPATH,"//div[@class = 'datepicker-days']/table/tbody/tr/td[@class = 'day']")
    DESIRED_DATE = (By.XPATH,"//div[@id = 'datepicker']/input")
    #URL
    URL = "http://www.webdriveruniversity.com/Datepicker/index.html"     

    def month_to_number(self,mon_in_num):
        monthdata = {
             1 : 'Jan',
             2 : 'Feb',
             3 : 'Mar',
             4 : 'Apr',
             5 : 'May',
             6 : 'Jun',
             7 : 'Jul',
             8 : 'Aug',
             9 : 'Sep',
             10 : 'Oct',
             11 : 'Nov',
             12 : 'Dec'
        }
        return monthdata[mon_in_num]

    def loadpage(self):
        self.browser.get(self.URL)

    def pickcalendardate(self,date_to_select):
        mon_day_year = date_to_select.split('-')
        targetmonth = self.month_to_number(int(mon_day_year[0]))

        calendar_button = self.browser.find_element(*self.CALENDAR_OPEN_BUTTON)
        calendar_button.click()

        month_display = self.browser.find_element(*self.MONTH_DISPLAY_SECTION)
        month_display.click()

        selected_year = self.browser.find_element(*self.SELECTED_CAL_YEAR)
        selectedYear = selected_year.text

        while selectedYear != mon_day_year[2]:

            if int(selectedYear) > int(mon_day_year[0]):
                previousbutton = self.browser.find_element(*self.PREVIOUS_BUTTON)
                previousbutton.click()
                selected_year = self.browser.find_element(*self.SELECTED_CAL_YEAR)
                selectedYear = selected_year.text
            else:
                nextbutton = self.browser.find_element(*self.NEXT_BUTTON)
                nextbutton.click()
                selected_year = self.browser.find_element(*self.SELECTED_CAL_YEAR)
                selectedYear = selected_year.text
        time.sleep(5)
        self.browser.get_screenshot_as_file("yearselected.png")
        
        calendarmonths = self.browser.find_elements(*self.CALENDAR_MONTHS)
        for months in calendarmonths:
            if months.text == targetmonth:
                months.click()
                self.browser.save_screenshot("monthselected.png")
                break
        
        time.sleep(5)
        
        calendarday = self.browser.find_elements(*self.CALENDAR_DAYS)
        for day in calendarday:
            if day.text == mon_day_year[1]:
                day.click()
                break
        
        self.browser.save_screenshot("desireddateselected.png")
        time.sleep(5)
        
        date = self.browser.find_element(*self.DESIRED_DATE)
        arrived_date = date.get_attribute("value")
        return arrived_date
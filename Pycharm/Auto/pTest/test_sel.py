from pytest import mark
from selenium import webdriver


# @mark.ui
# @mark.smoke
# @mark.color
def test_color(driver):
    driver.get('https://www.w3schools.com/colors/colors_picker.asp')
    pass
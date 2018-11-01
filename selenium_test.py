from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

driver = webdriver.Chrome()
driver.get("http://204.209.76.196:8000")

def test_home():
    # grab the elements for testing
    assert driver.find_element_by_id("name") != None
    assert driver.find_element_by_id("about") != None
    assert driver.find_element_by_id("skills") != None
    assert driver.find_element_by_id("education") != None
    assert driver.find_element_by_id("work") != None
    assert driver.find_element_by_id("contact") != None
    return

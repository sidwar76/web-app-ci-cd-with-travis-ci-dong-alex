from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

def test_home():
    # grab the elements for testing
    driver = webdriver.Chrome()
    driver.get("http://http://204.209.76.196:8000")
    driver.implicitly_wait(10)
    name_element = driver.find_element_by_id("name").text
    assert name_element != None
    driver.implicitly_wait(10)
    about_element = driver.find_element_by_id("about").text
    assert about_element != None
    skills_element = driver.find_element_by_id("skills").text
    education_element = driver.find_element_by_id("education").text
    work_element = driver.find_element_by_id("work").text
    contact_element = driver.find_element_by_id("contact").text

    # test the taken given
    
    
    assert skills_element != None
    assert education_element != None
    assert work_element != None
    assert contact_element != None
    return
    
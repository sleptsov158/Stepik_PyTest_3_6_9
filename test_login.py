import time

import pytest
import allure
from selenium import webdriver


# @pytest.fixture(scope="function")
# def browser():
#     chrome_options = webdriver.ChromeOptions()
#     browser = webdriver.Remote(
#         command_executor='http://selenoid:4444/wd/hub',
#         desired_capabilities={'browserName': 'chrome',
#                               'version': '92.0'},
#         options=chrome_options)
#     browser.implicitly_wait(10)
#     browser.maximize_window()
#
#     yield browser
#     browser.quit()

# @pytest.fixture()
# def test_setup():
#     global driver
#     driver = webdriver.Chrome()
#     driver.implicitly_wait(10)
#     driver.maximize_window()
#     yield
#     driver.quit()


@allure.description("Validates Stepik with valid values")
@allure.severity(severity_level="CRITICAL")
def test_login(browser):
    browser.get("https://stepik.org/lesson/25969/step/12")
    browser.maximize_window()
    browser.implicitly_wait(10)
    browser.find_element_by_xpath("//textarea").send_keys("get()")
    browser.implicitly_wait(10)
    submit_button = browser.find_element_by_xpath('//button[text()="Submit"]')
    time.sleep(10)
    submit_button.click()
    browser.implicitly_wait(10)
    browser.find_element_by_xpath('//label[text()="Password"]')


# @allure.description("Validates Stepik with invalid values")
# @allure.severity(severity_level="NORMAL")
# def test_invalid_login(test_setup):
#     driver.get("https://stepik.org/lesson/25969/step/12")
#     enter_value("got()")
#     submit_button = driver.find_element_by_css_selector(".submit-submission")
#     submit_button.click()
#     try:
#         assert driver.find_element_by_css_selector(".attempt-message_correct")
#     finally:
#         if AssertionError:
#             allure.attach(driver.get_screenshot_as_png(), name="Invalid value in stepik",
#                           attachment_type=allure.attachment_type.PNG)
#
#
# @allure.step("entering value")
# def enter_value(value):
#     browser.find_element_by_xpath("//textarea").send_keys(value)


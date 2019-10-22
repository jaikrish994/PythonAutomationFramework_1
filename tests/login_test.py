from selenium import webdriver
import moment
import allure
import pytest
from pages.homePage import HomePage
from pages.loginPage import LoginPage
from utils import utils as util
@pytest.mark.usefixtures("test_setup")
class TestLogin():
    def test_login(self):
        driver = self.driver
        driver.get(util.URL)
        login = LoginPage(driver)
        login.enter_username(util.USERNAME)
        login.enter_password(util.PASSWORD)
        login.click_login()
        # driver.find_element_by_id("txtUsername").send_keys("Admin")
        # driver.find_element_by_id("txtPassword").send_keys("admin123")
        # driver.find_element_by_id("btnLogin").click()
    def test_logout(self, test_setup):
        try:
            driver = self.driver
            homepage = HomePage(driver)
            homepage.click_welcome()
            homepage.click_logout()
            x = driver.title
            assert x == "abc"
        except AssertionError as error:
            print("Assertion Error Occured")
            print(error)
            currTime = moment.now().strftime("%d-%m-%y_%H-%M-%S")
            testName = util.whoami()
            screenshotName = testName+"_"+currTime
            allure.attach(self.driver.get_screenshot_as_png(),name=screenshotName,attachment_type=allure.attachment_type.PNG)
            driver.get_screenshot_as_file("C:/Users/computer/PycharmProjects/AutomationFramework_1/screenshots/ " + screenshotName + ".png")
            raise
        except:
            print("There was an Exception")
            currTime = moment.now().strftime("%d-%m-%y_%H-%M-%S")
            testName = util.whoami()
            screenshotName = testName + "_" + currTime
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,attachment_type=allure.attachment_type.PNG)
            driver.get_screenshot_as_file("C:/Users/computer/PycharmProjects/AutomationFramework_1/screenshots " + screenshotName + ".png")
            raise
        else:
            print("No Exception Occured")

        finally:
            print("I am inside finally Block")

        # driver.find_element_by_id("welcome").click()
        # driver.find_element_by_link_text("Logout").click()

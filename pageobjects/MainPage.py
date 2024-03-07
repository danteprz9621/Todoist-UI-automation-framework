import time
from selenium.webdriver import Keys
from locators.MainPageLocators import MainPageLocators
from pageobjects.BasePage import BasePage
from selenium.webdriver.common.keys import Keys


class MainPage(BasePage):

    def create_task(self):
        hover_div = self.driver.find_element(*MainPageLocators.new_task_div)
        self.helper.mouseover_element(hover_div)
        new_task_field = self.driver.find_element(*MainPageLocators.new_task_text_field)
        new_task_field.click()
        new_task_field.send_keys("First task")
        new_task_field.send_keys(Keys.ENTER)
        time.sleep(5)






import time
from selenium.webdriver import Keys
from locators.MainPageLocators import MainPageLocators
from pageobjects.BasePage import BasePage
from selenium.webdriver.common.keys import Keys


class MainPage(BasePage):

    def create_tasks(self, log, n=1):
        for i in range(n):
            log.info("Creating task " + str(i + 1))
            hover_div = self.driver.find_element(*MainPageLocators.new_task_div)
            self.helper.mouseover_element(hover_div)
            new_task_field = self.driver.find_element(*MainPageLocators.new_task_text_field)
            new_task_field.click()
            new_task_field.send_keys("Task number " + str(i + 1))
            new_task_field.send_keys(Keys.ENTER)
        time.sleep(5)

    def get_number_uncompleted_tasks(self):
        uncompleted_tasks = self.driver.find_elements(*MainPageLocators.task_list_items)
        return len(uncompleted_tasks)

    def delete_tasks(self, log, n=1):
        tasks = self.driver.find_elements(*MainPageLocators.task_list_items)
        log.info("List has " + str(len(tasks)) + " tasks")
        for i in range(n):
            log.info("Deleting task " + str(i + 1))
            self.helper.mouseover_element(tasks[i])
            delete_button = self.driver.find_element(*MainPageLocators.task_delete_button)
            delete_button.click()
        time.sleep(5)

    def create_specific_task(self, log, task_name):
        log.info("Creating task :" + task_name)
        hover_div = self.driver.find_element(*MainPageLocators.new_task_div)
        self.helper.mouseover_element(hover_div)
        new_task_field = self.driver.find_element(*MainPageLocators.new_task_text_field)
        new_task_field.click()
        new_task_field.send_keys(task_name)
        new_task_field.send_keys(Keys.ENTER)
        time.sleep(5)

    def delete_specific_task(self, log, task_name):
        tasks = self.driver.find_elements(*MainPageLocators.task_list_items)
        delete_buttons = self.driver.find_elements(*MainPageLocators.task_delete_button)
        log.info("List has " + str(len(tasks)) + " tasks")

        for i in range(len(tasks)):
            task_text = tasks[i].text
            task_text = task_text[:-2]
            if task_text == task_name:
                self.helper.mouseover_element(tasks[i])

                log.info("Deleting task :" + task_name)
                delete_buttons[i].click()
                time.sleep(5)
                break


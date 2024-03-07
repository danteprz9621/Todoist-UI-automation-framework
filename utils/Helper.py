from selenium.webdriver.common.action_chains import ActionChains


class Helper:

    def __init__(self, driver):
        self.driver = driver

    def mouseover_element(self, element):
        a = ActionChains(self.driver)
        a.move_to_element(element).perform()

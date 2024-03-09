import inspect

from selenium.webdriver.common.action_chains import ActionChains


class Helper:

    def __init__(self, driver):
        self.driver = driver

    def mouseover_element(self, element):
        a = ActionChains(self.driver)
        a.move_to_element(element).perform()

    def write_testname_log(self,log):
        test_name = inspect.stack()[1].function
        log.info("Executing test: " + test_name)




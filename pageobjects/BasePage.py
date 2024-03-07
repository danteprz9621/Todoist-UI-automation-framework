from utils.Helper import Helper


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.helper = Helper(self.driver)



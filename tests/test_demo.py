from assertpy import assert_that
from pageobjects.MainPage import MainPage
from utils.BaseTest import BaseTest


class TestTodoist(BaseTest):

    def test_basic(self, log):
        assert_that(1).is_equal_to(1)
        log.info("Test completed")

    def test_create_task(self, log):
        log.info("Starting test")
        main_page = MainPage(self.driver)
        main_page.create_task()
        log.info("Test completed")




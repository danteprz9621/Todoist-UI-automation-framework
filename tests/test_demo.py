import pytest
from assertpy import assert_that
from pageobjects.MainPage import MainPage
from utils.BaseTest import BaseTest


class TestTodoist(BaseTest):

    def test_basic(self, log):
        log.info("Starting test")
        assert_that(1).is_equal_to(1)
        log.info("Test completed")


class TestTaskCreation(BaseTest):
    def test_create_n_tasks(self, log):
        main_page = MainPage(self.driver)
        main_page.helper.write_testname_log(log)
        log.info("Starting test")
        main_page.create_tasks(log, 10)
        assert_that(main_page.get_number_uncompleted_tasks()).is_equal_to(10)
        log.info("Test completed")


class TestTaskDeletion(BaseTest):
    def test_delete_n_tasks(self, log):
        main_page = MainPage(self.driver)
        main_page.helper.write_testname_log(log)
        log.info("Starting test")
        main_page.create_tasks(log, 10)
        main_page.delete_tasks(log)
        #TODO: Update framework to data-driven one, delete hardcoded numbers
        assert_that(main_page.get_number_uncompleted_tasks()).is_equal_to(9)
        log.info("Test completed")
from assertpy import assert_that
from utils.BaseTest import BaseTest


class TestTodoist(BaseTest):
    def test_basic(self, log):
        assert_that(1).is_equal_to(1)
        log.info("Test completed")


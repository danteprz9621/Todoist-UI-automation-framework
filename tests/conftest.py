from selenium import webdriver
from loguru import logger
import pytest


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()

    driver.implicitly_wait(10)
    driver.get("https://microsoftedge.github.io/Demos/demo-to-do/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()


@pytest.fixture()
def log():
    logger.add("logs/todoist.log", level="INFO")
    yield logger

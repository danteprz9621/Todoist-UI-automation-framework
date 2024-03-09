import os
from datetime import datetime

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


@pytest.fixture(scope="session")
def log():
    start_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = "logs/" + str(start_time) + ".log"
    logger.add(file_name, level="INFO")
    yield logger


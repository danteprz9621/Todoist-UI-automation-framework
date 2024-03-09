import pytest


@pytest.mark.usefixtures("setup")
@pytest.mark.usefixtures("log")
class BaseTest:
    pass


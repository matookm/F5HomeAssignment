from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest


@pytest.fixture()
def setup_and_teardown():
    url = 'https://the-internet.herokuapp.com/context_menu'
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url)
    yield driver.page_source
    driver.quit()


def test_string_shown(setup_and_teardown):
    visible_string = 'Right-click in the box below to see one called \'the-internet\''
    assert visible_string in setup_and_teardown


def test_missing_string(setup_and_teardown):
    missing_string = 'Alibaba'
    assert missing_string in setup_and_teardown

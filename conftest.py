import time
from selenium.webdriver.support import expected_conditions as EC
import pytest
from appium.webdriver.common.appiumby import AppiumBy
from pytest_bdd import given
from selenium.webdriver.support.wait import WebDriverWait

from appium import webdriver

from helpers.get_capabilities import get_capabilities
from tests.pages.base_page import BasePage


def pytest_addoption(parser):
    parser.addoption('--env', default='android')


@pytest.fixture(scope="session")
def driver(request):
    env = request.config.getoption("env")
    capabilities = get_capabilities(env)

    # Note: Using desired_capabilities instead of options
    driver = webdriver.Remote('http://localhost:4723', options=capabilities)

    if env == 'android':
        try:
            accept_button = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((AppiumBy.ID, 'com.android.chrome:id/terms_accept'))
            )
            accept_button.click()

            negative_button = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((AppiumBy.ID, 'com.android.chrome:id/negative_button'))
            )
            negative_button.click()

            time.sleep(6)
            driver.switch_to.context('WEBVIEW_chrome')
        except Exception as e:
            print(f"Error during setup: {e}")
            driver.quit()
            raise

    yield driver

    # Teardown
    driver.quit()

@given("I open practice page")
def open_practice_page(driver):
    base_page = BasePage(driver)
    base_page.open_website()
    base_page.scroll_to_logo()
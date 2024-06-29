import time
from selenium.webdriver.support import expected_conditions as EC
import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from appium import webdriver
from helpers.get_capabilities import get_capabilities
from tests.steps.test_common_steps import *


def pytest_addoption(parser):
    parser.addoption('--env', default='android')


@pytest.fixture(scope="session")
def driver(request):
    env = request.config.getoption("env")
    capabilities = get_capabilities(env)

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

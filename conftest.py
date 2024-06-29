from time import sleep

import pytest
from appium.webdriver.common.appiumby import AppiumBy
from pytest_bdd import given

from config.ios_capabilities import ios_capabilities
from config.android_capabilities import android_capabilities
from appium import webdriver

def get_capabilities(env):
    if env == 'android':
        return android_capabilities()
    elif env == 'ios':
        return ios_capabilities()
    else:
        raise ValueError(f"Environment '{env}' is not supported.")


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
            # Wait for elements to be present and interactable
            accept_button = driver.find_element(by=AppiumBy.ID, value='com.android.chrome:id/terms_accept')
            accept_button.click()

            negative_button = driver.find_element(by=AppiumBy.ID, value='com.android.chrome:id/negative_button')
            negative_button.click()

            sleep(3)
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
    driver.get('https://rahulshettyacademy.com/AutomationPractice/')

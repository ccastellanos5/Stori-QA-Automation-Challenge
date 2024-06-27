from appium.webdriver.common.appiumby import AppiumBy
from time import sleep
import pytest


@pytest.mark.usefixtures('driver')
def test_android_skip_welcome_screen(driver):
    accept_button = driver.find_element(by=AppiumBy.ID, value='com.android.chrome:id/terms_accept')
    accept_button.click()

    negative_button = driver.find_element(by=AppiumBy.ID, value='com.android.chrome:id/negative_button')
    negative_button.click()


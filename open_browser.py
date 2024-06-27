from appium import webdriver
from appium.options.ios import XCUITestOptions
from appium.options.android import UiAutomator2Options
from time import sleep
from appium.webdriver.common.appiumby import AppiumBy


def open_browser_on_android():
    desired_caps = UiAutomator2Options()
    desired_caps.platformName = 'Android'
    desired_caps.platformVersion = '12.0'
    desired_caps.deviceName = 'emulator-5554'
    desired_caps.app_package = 'com.android.chrome'
    desired_caps.app_activity = 'com.google.android.apps.chrome.Main'
    desired_caps.automationName = 'UiAutomator2'
    desired_caps.noReset = 'true'


    appium_server_url = 'http://localhost:4723'

    driver = webdriver.Remote(appium_server_url, options=desired_caps)
    driver.get('https://rahulshettyacademy.com/AutomationPractice/')
    
    accept_button = driver.find_element(by=AppiumBy.ID, value='com.android.chrome:id/terms_accept')
    accept_button.click()

    negative_button = driver.find_element(by=AppiumBy.ID, value='com.android.chrome:id/negative_button')
    negative_button.click()

    sleep(15)
    driver.quit()
    

def open_browser_on_ios():
    desired_caps = XCUITestOptions()
    desired_caps.platformName = 'IOS'
    desired_caps.platformVersion = '17.5'
    desired_caps.deviceName = 'iPhone 15'
    desired_caps.browserName = 'Safari'
    desired_caps.automationName = 'XCUITest'
    desired_caps.noReset = 'true'

    appium_server_url = 'http://localhost:4723'

    driver = webdriver.Remote(appium_server_url, options=desired_caps)
    driver.get('https://rahulshettyacademy.com/AutomationPractice/')
    sleep(10)
    driver.quit()

if __name__ == "__main__":
    platform = input("Ingrese la plataforma (android/ios): ").strip().lower()
    if platform == "android":
        open_browser_on_android()
    elif platform == "ios":
        open_browser_on_ios()
    else:
        print("Plataforma no soportada. Por favor, ingrese 'android' o 'ios'.")

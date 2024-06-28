from appium.options.android import UiAutomator2Options
from webdriver_manager.chrome import ChromeDriverManager
def android_capabilities():
    chromedriver_path = ChromeDriverManager(driver_version="91.0.4472.101").install()
    desired_caps = UiAutomator2Options()
    desired_caps.platformName = 'Android'
    desired_caps.platformVersion = '12.0'
    desired_caps.deviceName = 'emulator-5554'
    desired_caps.app_package = 'com.android.chrome'
    desired_caps.app_activity = 'com.google.android.apps.chrome.Main'
    desired_caps.automationName = 'UiAutomator2'
    desired_caps.auto_web_view = 'true'
    desired_caps.chromedriver_executable = chromedriver_path
    return desired_caps

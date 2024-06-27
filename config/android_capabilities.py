from appium.options.android import UiAutomator2Options


def android_capabilities():
    desired_caps = UiAutomator2Options()
    desired_caps.platformName = 'Android'
    desired_caps.platformVersion = '12.0'
    desired_caps.deviceName = 'emulator-5554'
    desired_caps.app_package = 'com.android.chrome'
    desired_caps.app_activity = 'com.google.android.apps.chrome.Main'
    desired_caps.automationName = 'UiAutomator2'
    desired_caps.noReset = 'true'
    desired_caps.auto_web_view = 'true'

    return desired_caps

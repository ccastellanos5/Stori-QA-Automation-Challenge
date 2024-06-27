from appium.options.ios import XCUITestOptions


def ios_capabilities():
    desired_caps = XCUITestOptions()
    desired_caps.platformName = 'IOS'
    desired_caps.platformVersion = '17.5'
    desired_caps.deviceName = 'iPhone 15'
    desired_caps.browserName = 'Safari'
    desired_caps.automationName = 'XCUITest'
    desired_caps.noReset = 'true'
    desired_caps.auto_web_view = 'true'

    return desired_caps

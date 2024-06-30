
import pytest
from pytest_bdd import when, parsers, scenarios, then

from tests.pages.switch_to_alert_page import SwitchToAlertPage
from tests.selectors.switch_to_alert_selectors import *

scenarios('../features/switch_to_alert.feature')


@pytest.mark.usefixtures("driver")
@when(parsers.parse('I type "{expected_text}" into the alert input'))
def enter_text_in_alert(driver, expected_text):
    switch_to_alert_page = SwitchToAlertPage(driver)
    switch_to_alert_page.enter_text_in_alert_input(expected_text)


@pytest.mark.usefixtures("driver")
@when(parsers.parse('I click the "{button_name}" button'))
def click_button_of_switch_alert_section(driver, button_name):
    switch_to_alert_page = SwitchToAlertPage(driver)
    if button_name == 'alert':
        switch_to_alert_page.click_the_alert_button(ALERT_BUTTON_XPATH)
    elif button_name == 'confirm':
        switch_to_alert_page.click_the_alert_button(CONFIRM_BUTTON_XPATH)


@pytest.mark.usefixtures("driver")
@then(parsers.parse('I should see an alert with the text "{expected_text}"'))
def validate_alert_with_expected_message(driver, expected_text):
    switch_to_alert_page = SwitchToAlertPage(driver)
    current_text = switch_to_alert_page.get_text_from_alert()
    assert current_text == expected_text



@pytest.mark.usefixtures("driver")
@then('I print the alert text')
def print_alert_text_in_console(driver):
    switch_to_alert_page = SwitchToAlertPage(driver)
    print(switch_to_alert_page.get_text_from_alert())


@pytest.mark.usefixtures("driver")
@then(parsers.parse('I "{alert_action}" the alert'))
def close_alert_with_action(driver, alert_action):
    switch_to_alert_page = SwitchToAlertPage(driver)
    if alert_action == 'accept':
        switch_to_alert_page.accept_alert()
    elif alert_action == 'confirm':
        switch_to_alert_page.dismiss_alert()









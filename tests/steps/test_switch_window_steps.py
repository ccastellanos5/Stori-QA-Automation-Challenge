import pytest
from pytest_bdd import scenarios, when, then, parsers, given
from tests.pages.switch_window_page import SwitchWindowPage

scenarios('../features/switch_window.feature')


@pytest.mark.usefixtures("driver")
@when('I click the open window button')
def click_open_window(driver):
    switch_window_page = SwitchWindowPage(driver)
    switch_window_page.click_open_window_button()


@pytest.mark.usefixtures("driver")
@then(parsers.parse('I should see "{expected_guarantee_text}" text displayed in the new window'))
def validate_the_guarantee_text_appears(driver, expected_guarantee_text):
    switch_window_page = SwitchWindowPage(driver)
    switch_window_page.redirect_to_new_window(2)
    current_displayed_text = switch_window_page.get_guarantee_text(expected_guarantee_text)
    assert current_displayed_text is not None


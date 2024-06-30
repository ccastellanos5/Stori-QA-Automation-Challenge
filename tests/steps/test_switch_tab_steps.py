import pytest
from pytest_bdd import scenarios, when, given, then

from tests.pages.switch_tab_page import SwitchTabPage
from tests.selectors.switch_tab_selectors import UPCOMING_EVENT_SECTION

scenarios('../features/switch_tab.feature')


@pytest.mark.usefixtures("driver")
@when('I click the open tab button')
def click_open_window(driver):
    switch_window_page = SwitchTabPage(driver)
    switch_window_page.click_open_tap_button()


@pytest.mark.usefixtures("driver")
@then('I should be redirected to QAClick Academy')
def redirect_to_qa_click_academy(driver):
    switch_window_page = SwitchTabPage(driver)
    switch_window_page.redirect_to_qa_click_academy()


@pytest.mark.usefixtures("driver")
@then('I scroll to the Upcoming events section')
def scroll_to_section_upcoming_events_section(driver):
    switch_window_page = SwitchTabPage(driver)
    element = switch_window_page.find_element_by_xpath(UPCOMING_EVENT_SECTION)
    switch_window_page.scroll_to_an_element_with_js(element)


@pytest.mark.usefixtures("driver")
@then('I should be able to take a screenshot')
def take_screenshot(driver):
    switch_window_page = SwitchTabPage(driver)
    switch_window_page.take_screenshot_of_upcoming_event('switch_tab.feature')

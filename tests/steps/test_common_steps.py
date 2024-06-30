import time

import pytest
from pytest_bdd import given, then
from tests.pages.base_page import BasePage


@pytest.mark.usefixtures('driver')
@given("I open practice page")
def open_practice_page(driver):
    base_page = BasePage(driver)
    base_page.open_website()
    base_page.scroll_to_logo()


@pytest.mark.usefixtures('driver')
@then("I go back to the practice page")
def back_to_practice_page(driver):
    base_page = BasePage(driver)
    base_page.return_to_original_window()

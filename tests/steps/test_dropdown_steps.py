import pytest
from pytest_bdd import scenarios, when, then, parsers
from tests.pages.dropdown_page import DropdownPage

scenarios('../features/dropdown.feature')


@when(parsers.parse('I select "{option_value}" from the dropdown'))
@pytest.mark.usefixtures('driver')
def select_an_option_from_dropdown(driver, option_value):
    dropdown_page = DropdownPage(driver=driver)
    dropdown_page.click_over_dropdown()
    dropdown_page.select_option_from_dropdown(option_value)


@then(parsers.parse('I should see displayed "{option_value}"'))
@pytest.mark.usefixtures('driver')
def validate_option_selected(driver, option_value):
    dropdown_page = DropdownPage(driver=driver)
    current_dropdown_value = dropdown_page.get_selected_option()
    assert current_dropdown_value == option_value.lower()

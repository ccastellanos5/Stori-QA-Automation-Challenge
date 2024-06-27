from time import sleep

import pytest
from pytest_bdd import *
from tests.pages.suggestion_class_page import SuggestionClassPage

scenarios('../features/suggestion_class.feature')
@given('I move to the Suggestion Class Example page')
def scroll_until_section(driver):
    suggestion_class_page = SuggestionClassPage(driver=driver)
    suggestion_class_page.go_to_suggestion_class_section()


@pytest.mark.usefixtures("driver")
@when('I enter "Me" into the suggestion box')
def search_country_by_name(driver):
    suggestion_class_page = SuggestionClassPage(driver=driver)
    suggestion_class_page.input_country('Me')


@pytest.mark.usefixtures("driver")
@when('I select the country "Mexico" from the suggestions')
def select_country_suggestion(driver):
    suggestion_class_page = SuggestionClassPage(driver=driver)
    suggestion_class_page.select_country_from_suggestions('Mexico')


@pytest.mark.usefixtures("driver")
@then('the selected country should be "Mexico"')
def validate_the_country_selected(driver):
    suggestion_class_page = SuggestionClassPage(driver=driver)
    selected_country = suggestion_class_page.get_selected_country()
    assert selected_country == 'Mexico'

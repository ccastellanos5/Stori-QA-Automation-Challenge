import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from tests.pages.suggestion_class_page import SuggestionClassPage

scenarios('../features/suggestion_class.feature')


@pytest.mark.usefixtures("driver")
@when(parsers.parse('I enter "{country_prefix}" into the suggestion box'))
def search_country_by_name(driver, country_prefix):
    suggestion_class_page = SuggestionClassPage(driver=driver)
    suggestion_class_page.input_country(country_prefix)


@pytest.mark.usefixtures("driver")
@when(parsers.parse('I select the country "{country_name}" from the suggestions'))
def select_country_suggestion(driver, country_name):
    suggestion_class_page = SuggestionClassPage(driver=driver)
    suggestion_class_page.select_country_from_suggestions(country_name)


@pytest.mark.usefixtures("driver")
@then(parsers.parse('the selected country should be "{country_name}"'))
def validate_the_country_selected(driver, country_name):
    suggestion_class_page = SuggestionClassPage(driver=driver)
    selected_country = suggestion_class_page.get_selected_country()
    assert selected_country == country_name

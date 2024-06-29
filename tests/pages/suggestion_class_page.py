from tests.pages.base_page import BasePage
from tests.selectors.SuggestionClassSelectors import SUGGESTION_LIST_XPATH, INPUT_XPATH

class SuggestionClassPage(BasePage):
    def input_country(self, country):
        self.click_element_by_xpath(INPUT_XPATH)
        self.enter_value_by_xpath(INPUT_XPATH, country)
        self.hide_keyboard()

    def select_country_from_suggestions(self, country):
        suggestion_xpath = f"{SUGGESTION_LIST_XPATH}[contains(text(), '{country}')]"
        self.hide_keyboard()
        self.click_element_by_xpath(suggestion_xpath)
        self.hide_keyboard()

    def get_selected_country(self):
        input_element = self.find_element_by_xpath(INPUT_XPATH)
        input_value = self.driver.execute_script("return arguments[0].value;", input_element)
        return input_value
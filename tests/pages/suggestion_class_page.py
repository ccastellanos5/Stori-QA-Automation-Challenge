from tests.pages.base_page import BasePage
from tests.selectors.suggestion_class_selectors import SUGGESTION_LIST_XPATH, INPUT_XPATH


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
        return self.get_value_from_element_by_xpath(INPUT_XPATH)

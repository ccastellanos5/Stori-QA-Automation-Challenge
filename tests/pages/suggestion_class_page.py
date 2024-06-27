from selenium.webdriver.common.by import By
from tests.pages.base_page import BasePage
from tests.selectors.SuggestionClassSelectors import SUGGESTION_LIST_XPATH, INPUT_XPATH, SUGGESTION_CLASS_TITLE_XPATH


class SuggestionClassPage(BasePage):
    def input_country(self, country):
        self.click_element_by_xpath(INPUT_XPATH)
        self.enter_value_by_xpath(INPUT_XPATH, country)

    def select_country_from_suggestions(self, country):
        self.wait_element_by_xpath(SUGGESTION_LIST_XPATH)
        suggestion_xpath = f"{SUGGESTION_LIST_XPATH}[contains(text(), '{country}')]"
        self.click_element_by_xpath(suggestion_xpath)

    def get_selected_country(self):
        input_element = self.driver.find_element(By.XPATH, INPUT_XPATH)
        input_value = self.driver.execute_script("return arguments[0].value;", input_element)
        return input_value

    def go_to_suggestion_class_section(self):
        self.click_element_by_xpath(SUGGESTION_CLASS_TITLE_XPATH)
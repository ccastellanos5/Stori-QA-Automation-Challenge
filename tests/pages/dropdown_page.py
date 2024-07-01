import time

from tests.pages.base_page import BasePage
from tests.selectors.dropdown_selectors import DROPDOWN_XPATH, DROPDOWN_XPATH_OPTION


class DropdownPage(BasePage):

    def select_option_from_dropdown(self, option):
        option_xpath = DROPDOWN_XPATH_OPTION.format(option_value=option.lower())
        print("XPATH: ", option_xpath)
        self.click_element_by_xpath(option_xpath)

    def click_over_dropdown(self):
        self.click_element_by_xpath(DROPDOWN_XPATH)

    def get_selected_option(self):
        return self.get_value_from_element_by_xpath(DROPDOWN_XPATH)
from tests.pages.base_page import BasePage
from tests.selectors.switch_window_selectors import OPEN_WINDOW_BUTTON_XPATH


class SwitchWindowPage(BasePage):

    def click_open_window_button(self):
        self.click_element_by_xpath(OPEN_WINDOW_BUTTON_XPATH)

    def get_guarantee_text(self, expected_text):
        current_displayed_text = self.find_text_in_page(expected_text, 15)
        return current_displayed_text

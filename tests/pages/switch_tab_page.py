from tests.pages.base_page import BasePage
from tests.selectors.switch_tab_selectors import *


class SwitchTabPage(BasePage):

    def click_open_tap_button(self):
        self.click_element_by_css_selector(OPEN_TAB_BUTTON_CSS_SELECTOR)

    def redirect_to_qa_click_academy(self):
        self.redirect_to_new_window(2)
        logo = self.find_element_by_xpath(QA_CLICK_ACADEMY_LOGO, timeout=20)
        assert logo.is_displayed()

    def take_screenshot_of_upcoming_event(self, screenshot_name):
        path = f'{screenshot_name}.png'
        self.take_screenshot_and_save(path)


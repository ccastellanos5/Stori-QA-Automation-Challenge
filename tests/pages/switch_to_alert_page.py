import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from helpers.scripts import ON_CLICK
from tests.pages.base_page import BasePage
from tests.selectors.switch_to_alert_selectors import ALERT_INPUT_XPATH, ALERT_BUTTON_XPATH


class SwitchToAlertPage(BasePage):

    def enter_text_in_alert_input(self, text):
        self.enter_value_by_xpath(ALERT_INPUT_XPATH, text)

    def click_the_alert_button(self, button_name_xpath):
        button = self.find_element_by_xpath(button_name_xpath)
        self.driver.execute_script(ON_CLICK, button)

    def get_text_from_alert(self):
        alert = self.driver.switch_to.alert
        text = alert.text
        return text

    def accept_alert(self):
        alert = self.driver.switch_to.alert
        alert.accept()

    def dismiss_alert(self):
        alert = self.driver.switch_to.alert
        alert.dismiss()

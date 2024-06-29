import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("driver")
class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click_element_by_xpath(self, xpath):
        element = self.find_element_by_xpath(xpath)
        element.click()

    def enter_value_by_xpath(self, xpath, text):
        input_element = self.find_element_by_xpath(xpath)
        input_element.clear()
        input_element.send_keys(text)
        self.hide_keyboard()

    def hide_keyboard(self):
        self.driver.hide_keyboard()

    def find_element_by_xpath(self, xpath, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((By.XPATH, xpath))
        )
        return element

    def get_value_from_element_by_xpath(self, xpath):
        element = self.find_element_by_xpath(xpath)
        element_value = self.driver.execute_script("return arguments[0].value;", element)
        return element_value

    def find_text_in_page(self, expected_text, timeout=10):
        try:
            elements = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located((By.TAG_NAME, 'body'))
            )
            for element in elements:
                if expected_text in element.text:
                    return element.text
            return None
        except:
            return None

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers.scripts import SCROLL_SCRIPT
from tests.selectors.base_selectors import LOGO_XPATH


@pytest.mark.usefixtures("driver")
class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def open_website(self):
        self.driver.get('https://rahulshettyacademy.com/AutomationPractice/')

    def get_current_window(self):
        return self.driver.current_window_handle

    def return_to_original_window(self):
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def click_element_by_xpath(self, xpath):
        element = self.find_element_by_xpath(xpath)
        element.click()

    def click_element_by_css_selector(self, selector):
        element = self.find_element_by_css_selector(selector)
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

    def find_element_by_css_selector(self, selector, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, selector))
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

    def scroll_to_an_element_with_js(self, element):
        self.driver.execute_script(SCROLL_SCRIPT, element)

    def scroll_to_logo(self):
        logo = self.find_element_by_xpath(LOGO_XPATH)
        self.scroll_to_an_element_with_js(logo)

    def redirect_to_new_window(self, number_of_window_expected):
        WebDriverWait(self.driver, 10).until(
            EC.number_of_windows_to_be(number_of_window_expected)
        )
        new_window = self.driver.window_handles[number_of_window_expected - 1]
        self.driver.switch_to.window(new_window)

    def take_screenshot_and_save(self, path_file):
        self.driver.save_screenshot(path_file)

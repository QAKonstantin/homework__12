import logging
import allure

from dotenv import load_dotenv
from selenium import common
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from pathlib import Path


class BasePage:
    FOOTER = (By.ID, "footer")
    BREAD_CRUMBS = (By.CSS_SELECTOR, ".breadcrumb")
    SEARCH = (By.CSS_SELECTOR, "#search")
    ITEMS = (By.CSS_SELECTOR, "#cart-total")
    LOGO = (By.ID, "logo")
    CONTENT = (By.ID, "content")
    TOP = (By.CSS_SELECTOR, "#top")

    def __init__(self, browser, wait=3):
        self.browser = browser
        self.wait = WebDriverWait(browser, wait)
        self.actions = ActionChains(browser)
        load_dotenv()
        self.__config_logger()

    def __config_logger(self):
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.addHandler(
            logging.FileHandler(f"{Path(__file__).resolve().parent.parent}/logs/{self.browser.test_name}.log"))
        self.logger.setLevel(level=self.browser.log_level)

    @allure.step("Input text: '{text}'")
    def _input_text(self, web_element, text):
        self.logger.info(f"Input '{text}'")
        web_element.clear()
        web_element.send_keys(text)

    @allure.step("Search an element: '{locator}'")
    def _search_element(self, locator: tuple, timeout=2):
        self.logger.info("Check if element {} was found".format(locator))
        try:
            return WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            allure.attach(
                name=self.browser.session_id,
                body=self.browser.get_screenshot_as_png(),
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError(f"Cant find element by locator: {locator}")

    @allure.step("Search link text: '{link_text}'")
    def _search_link_text(self, link_text, timeout=2):
        try:
            self.logger.info("Check if link text {} was found".format(link_text))
            return WebDriverWait(self.browser, timeout) \
                .until(EC.visibility_of_element_located((By.LINK_TEXT, link_text)))
        except TimeoutException:
            self.logger.warning("Cant find element by link text: {}".format(link_text))
            allure.attach(
                name=self.browser.session_id,
                body=self.browser.get_screenshot_as_png(),
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError("Cant find element by link text: {}".format(link_text))

    @allure.step("Wait text element with text: '{goal}'")
    def _wait_text_element(self, locator, goal, timeout=2):
        self.logger.info(f"Check if element {locator} is present")
        try:
            WebDriverWait(self.browser, timeout).until(EC.text_to_be_present_in_element(locator, goal))
        except common.exceptions.TimeoutException:
            allure.attach(
                name=self.browser.session_id,
                body=self.browser.get_screenshot_as_png(),
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError(f"Cant find element by locator: {locator}")

    def _click_link(self, link_text):
        self._click((By.LINK_TEXT, link_text))
        return self

    @allure.step("Click an element '{locator}'")
    def _click(self, locator: tuple):
        self.logger.info(f"Clicking element: {locator}")
        self.element = self._element(locator)
        self.element.click()
        return self.element

    def _element(self, locator: tuple):
        return self._search_element(locator)

    @allure.step("Open url {path}")
    def open(self, path):
        self.logger.info("Opening url: {}".format(self.browser.url + path))
        self.browser.get(self.browser.current_url + path)
        return self

    @allure.step("Verify element {css_selector} on page.")
    def check_element_presence(self, css_selector):
        try:
            self.browser.find_element_by_css_selector(css_selector)
        except common.exceptions.NoSuchElementException:
            allure.attach(
                name=self.browser.session_id,
                body=self.browser.get_screenshot_as_png(),
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError(f"Element {css_selector} not found on page!")

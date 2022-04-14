from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class MainPage(BasePage):
    SLIDESHOW = (By.CSS_SELECTOR, "#slideshow0")
    CAROUSEL = (By.CSS_SELECTOR, "#carousel0")
    ROW = (By.CSS_SELECTOR, ".row")
    NAVIGATION_BAR = (By.CSS_SELECTOR, "[class='collapse navbar-collapse navbar-ex1-collapse']")

    def check_elements(self):
        self._element(self.SLIDESHOW)
        self._element(self.CAROUSEL)
        self._element(self.SEARCH)
        self._element(self.ROW)
        self._element(self.NAVIGATION_BAR)
        self._element(self.LOGO)
        self._wait_text_element(self.ITEMS, "0 item(s) - $0.00")
        self._wait_text_element(self.CONTENT, "Featured")

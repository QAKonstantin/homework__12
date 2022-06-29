import allure
from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class AdminNavigation(BasePage):
    CATALOG = (By.CSS_SELECTOR, "#menu-catalog")
    PRODUCTS = (By.CSS_SELECTOR, "#collapse1 > li:nth-child(2) > a")

    @allure.step("Move to products")
    def move_to_products(self):
        self._element(self.CATALOG).click()
        self._element(self.PRODUCTS).click()

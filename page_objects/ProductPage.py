from selenium.webdriver.common.by import By

from page_objects.BasePage import BasePage


class ProductPage(BasePage):
    PRODUCT_DESCRIPTION = (By.CSS_SELECTOR, "div[id='tab-description']")
    INPUT_QUANTITY = (By.CSS_SELECTOR, "#input-quantity")
    ACTIVE = (By.CLASS_NAME, "active")
    ADD_TO_CART = (By.ID, "button-cart")
    PRODUCT_NAME = (By.CSS_SELECTOR, "#content > div > div.col-sm-4 > h1")

    def check_elements(self, path, product_name):
        self.open(path)
        self._element(self.SEARCH)
        self._element(self.TOP)
        self._element(self.PRODUCT_DESCRIPTION)
        self._element(self.INPUT_QUANTITY)
        self._element(self.BREAD_CRUMBS)
        self._wait_text_element(self.PRODUCT_NAME, product_name)
        self._wait_text_element(self.ACTIVE, "Description")
        self._wait_text_element(self.ADD_TO_CART, "Add to Cart")

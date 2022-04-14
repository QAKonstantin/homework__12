import allure
from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class Header(BasePage):
    REGISTER_ICON = (By.LINK_TEXT, "My Account")
    DROPDOWN_CURRENCY = (By.ID, "form-currency")

    @allure.step("Click to register")
    def click_to_register(self):
        self._click(self.REGISTER_ICON)
        self._click_link("Register")

    @allure.step("Change currency {currency}")
    def change_currency(self, currency):
        self._element(self.DROPDOWN_CURRENCY).click()
        self._element((By.CSS_SELECTOR, "button[name='{}']".format(currency))).click()

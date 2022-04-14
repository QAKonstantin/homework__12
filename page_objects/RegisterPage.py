import allure
from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class RegisterPage(BasePage):
    INPUT_FIRSTNAME = (By.ID, "input-firstname")
    INPUT_LASTNAME = (By.ID, "input-lastname")
    INPUT_EMAIL = (By.ID, "input-email")
    INPUT_TELEPHONE = (By.ID, "input-telephone")
    INPUT_PASSWORD = (By.ID, "input-password")
    CONFIRM_PASSWORD = (By.ID, "input-confirm")
    AGREEMENT = (By.CLASS_NAME, "modal-title")
    LINK_AGREEMENT = (By.CLASS_NAME, "agree")
    BUTTON_CONTINUE = (By.CSS_SELECTOR, "input[type='submit'][value='Continue']")
    SUBSCRIBE = (By.CSS_SELECTOR, ".radio-inline input[value='1']")
    RULES = (By.NAME, "agree")
    BUTTON_CLOSE = (By.CLASS_NAME, "close")
    BUTTON_COMPLETE = (By.CSS_SELECTOR, "#content > div > div > a")
    ACCOUNT = (By.ID, "account-account")

    @allure.step("Input personal details")
    def input_personal_details(self, firstname, lastname, email, phone, password):
        self._input_text(self._element(self.INPUT_FIRSTNAME), firstname)
        self._input_text(self._element(self.INPUT_LASTNAME), lastname)
        self._input_text(self._element(self.INPUT_EMAIL), email)
        self._input_text(self._element(self.INPUT_TELEPHONE), phone)
        self._input_text(self._element(self.INPUT_PASSWORD), password)
        self._input_text(self._element(self.CONFIRM_PASSWORD), password)

    @allure.step("Subscribe to the rools")
    def subscribe(self):
        self._element(self.SUBSCRIBE).click()

    @allure.step("Open agreement")
    def open_agreement(self):
        self._element(self.LINK_AGREEMENT).click()

    @allure.step("Close agreement")
    def close_agreement(self):
        self._wait_text_element(self.AGREEMENT, "Privacy Policy", 5)
        self._element(self.BUTTON_CLOSE).click()

    @allure.step("Agree to the rules")
    def rules_agree(self):
        self._element(self.RULES).click()

    @allure.step("Сonfirm registration")
    def submit_register(self):
        self._element(self.BUTTON_CONTINUE).click()

    @allure.step("Completing registration")
    def complete_registration(self):
        self._element(self.BUTTON_COMPLETE).click()
        self._element(self.ACCOUNT)

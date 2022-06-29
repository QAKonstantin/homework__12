from selenium.webdriver.common.by import By
import allure
from page_objects.BasePage import BasePage
from page_objects.elements.AdminNavigation import AdminNavigation


class AdminPanel(BasePage):
    PATH = '/admin'
    INPUT_USERNAME = (By.CSS_SELECTOR, "#input-username")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "#input-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type=submit]")
    ADD_PRODUCT = (By.CSS_SELECTOR, "i[class='fa fa-plus']")
    DELETE_PRODUCT = (By.CSS_SELECTOR, "i[class='fa fa-trash-o']")
    INPUT_PRODUCT_NAME = (By.CSS_SELECTOR, "#input-name1")
    INPUT_MODEL_NAME = (By.CSS_SELECTOR, "#input-model")
    TAB_DATA = (By.CSS_SELECTOR, "a[href='#tab-data']")
    META_TAG_TITLE = (By.CSS_SELECTOR, "#input-meta-title1")
    SAVE = (By.CSS_SELECTOR, "button[type='submit']")
    PRODUCT_NAME = (By.CSS_SELECTOR, "input[name='filter_name']")
    BUTTON_FILTER = (By.CSS_SELECTOR, "#button-filter")
    PRODUCT_CHECKBOX = (By.CSS_SELECTOR, "input[type='checkbox']")
    ALERT = (By.CSS_SELECTOR, "i[class='fa fa-check-circle']")
    INPUT_FORM = (By.CSS_SELECTOR, ".input-group")
    BUTTON_LOGIN = (By.CSS_SELECTOR, "[class='btn btn-primary']")
    HELP = (By.CSS_SELECTOR, ".help-block")
    PANEL_BODY = (By.CSS_SELECTOR, ".panel-body")
    PANEL_HEAD = (By.CLASS_NAME, "panel-heading")

    @allure.step("Authorization with name {username}")
    def login_with(self, username, password):
        self.open(self.PATH)
        self._input_text(self._element(self.INPUT_USERNAME), username)
        self._input_text(self._element(self.INPUT_PASSWORD), password)
        self._element(self.LOGIN_BUTTON).click()

    @allure.step("Add product with name '{product_name}', model {model}")
    def add_product(self, product_name, model, tag):
        AdminNavigation(self.browser).move_to_products()
        self._element(self.ADD_PRODUCT).click()
        self._input_text(self._element(self.INPUT_PRODUCT_NAME), product_name)
        self._input_text(self._element(self.META_TAG_TITLE), tag)
        self._element(self.TAB_DATA).click()
        self._input_text(self._element(self.INPUT_MODEL_NAME), model)
        self._element(self.SAVE).click()

    @allure.step("Delete product with name '{product_name}'")
    def delete_product(self, product_name):
        self._input_text(self._element(self.PRODUCT_NAME), product_name)
        self._element(self.BUTTON_FILTER).click()
        self._element(self.PRODUCT_CHECKBOX).click()
        self._element(self.DELETE_PRODUCT).click()
        self.browser.switch_to.alert.accept()
        self._element(self.ALERT)

    def check_elements(self):
        self.open(self.PATH)
        self._element(self.INPUT_FORM)
        self._element(self.BUTTON_LOGIN)
        self._element(self.HELP)
        self._element(self.PANEL_BODY)
        self._wait_text_element(self.PANEL_HEAD, "Please enter your login details.")
        self._wait_text_element(self.FOOTER, " © 2009-2022 All Rights Reserved.")

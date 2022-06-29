import allure
from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class CategoryPage(BasePage):
    SORT_BY = (By.CSS_SELECTOR, ".input-group-addon")
    ICON_LIST = (By.CSS_SELECTOR, "[class='fa fa-th']")
    PC_BANNER = (By.CSS_SELECTOR, ".img-responsive")
    PHONE_CATEGORY = (By.CSS_SELECTOR, "[class='list-group-item active']")
    BLOCK_CATEGORY = (By.CSS_SELECTOR, "#column-left")

    @allure.step("Move to '{category}'")
    def move_to_categories(self, category, dropdown=''):
        self._search_link_text(category).click()
        if (dropdown != ''):
            self._search_link_text(dropdown).click()

    def check_elements_laptops(self):
        self._search_link_text("Laptops & Notebooks")
        self._element(self.SORT_BY)
        self._element(self.ICON_LIST)
        self._element(self.PC_BANNER)
        self._element(self.BREAD_CRUMBS)
        self._wait_text_element(self.CONTENT, "Refine Search")

    def check_elements_phones(self):
        self._search_link_text("Phones & PDAs")
        self._element(self.PHONE_CATEGORY)
        self._element(self.BLOCK_CATEGORY)
        self._element(self.SEARCH)
        self._element(self.CONTENT)
        self._element(self.ITEMS)
        self._wait_text_element(self.BREAD_CRUMBS, "Phones & PDAs")

    def check_elements_monitors(self):
        self._search_link_text("Monitors")
        self._element(self.BLOCK_CATEGORY)
        self._element(self.PC_BANNER)
        self._element(self.BREAD_CRUMBS)
        self._element(self.SEARCH)
        self._element(self.CONTENT)
        self._wait_text_element(self.CONTENT, "Monitors")

import allure
from page_objects.CategoryPage import CategoryPage


@allure.severity(allure.severity_level.NORMAL)
@allure.title("This test check elements on page Desktops")
def test_elements_laptops_category(browser):
    user = CategoryPage(browser)
    user.move_to_categories("Desktops", "Show All Desktops")
    user.check_elements_laptops()


@allure.severity(allure.severity_level.NORMAL)
@allure.title("This test check elements on page Phones & PDAs")
def test_elements_phones_category(browser):
    user = CategoryPage(browser)
    user.move_to_categories("Phones & PDAs")
    user.check_elements_phones()


@allure.title("This test check elements on page Monitors")
def test_elements_monitors_category(browser):
    user = CategoryPage(browser)
    user.move_to_categories("Components", "Monitors (2)")
    user.check_elements_monitors()

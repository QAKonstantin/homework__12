from page_objects.MainPage import MainPage
import allure


@allure.severity(allure.severity_level.NORMAL)
@allure.title("This test check elements on main page")
def test_check_main_page(browser):
    page = MainPage(browser)
    page.check_elements()

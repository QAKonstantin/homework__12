from page_objects.AdminPanelPage import AdminPanel
import os
import allure


@allure.severity(allure.severity_level.BLOCKER)
@allure.title("This test add/delete product by Administrator")
def test_add_delete_product(browser):
    admin = AdminPanel(browser)
    admin.login_with("user", os.getenv("ADMIN_PASSWORD"))
    admin.add_product(product_name="Test_name", model="Test_model", tag="test")
    admin.delete_product(product_name="Test_name")


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("This test check elements on Admin panel")
def test_check_page_admin(browser):
    page = AdminPanel(browser)
    page.check_elements()

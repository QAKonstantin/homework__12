from page_objects.ProductPage import ProductPage
import allure


@allure.severity(allure.severity_level.NORMAL)
@allure.title("This test check elements on product card iMac")
def test_check_card_imac(browser):
    page = ProductPage(browser)
    page.check_elements("/index.php?route=product/product&path=20_27&product_id=41", "iMac")


@allure.severity(allure.severity_level.NORMAL)
@allure.title("This test check elements on product card Nikon D300")
def test_check_card_nikon_d300(browser):
    page = ProductPage(browser)
    page.check_elements("/index.php?route=product/product&path=33&product_id=31", "Nikon D300")

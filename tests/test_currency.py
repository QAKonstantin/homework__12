from page_objects.elements.Header import Header
import allure


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("This test changes currency: EUR, GBR, USD")
def test_change_currency(browser):
    user = Header(browser)
    allure.dynamic.title('Change currency EUR')
    user.change_currency("EUR")
    allure.dynamic.title('Change currency GBP')
    user.change_currency("GBP")
    allure.dynamic.title('Change currency USD')
    user.change_currency("USD")

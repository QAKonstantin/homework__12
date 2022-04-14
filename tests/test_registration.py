import os
import allure
from page_objects.RegisterPage import RegisterPage
from page_objects.elements.Header import Header


@allure.severity(allure.severity_level.BLOCKER)
@allure.title("Registration new user with name {create_user[0]}")
def test_register_form(browser, create_user):
    user = RegisterPage(browser)
    Header(browser).click_to_register()
    user.input_personal_details(firstname="Adam", lastname="Jeferson", email=create_user[0],
                                phone=create_user[1], password=os.getenv("USER_PASSWORD"))
    user.subscribe()
    user.open_agreement()
    user.close_agreement()
    user.rules_agree()
    user.submit_register()
    user.complete_registration()

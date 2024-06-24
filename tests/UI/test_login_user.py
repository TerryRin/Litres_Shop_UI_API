import allure
from allure_commons.types import Severity

from litres_shop.pages.UI.login_page import login_page
from litres_shop.pages.UI.main_page import main_page


@allure.epic('Login')
@allure.title('Successful login user')
@allure.link('https://www.litres.ru/', name='litres')
@allure.tag('web')
@allure.severity(Severity.MINOR)
@allure.label('owner', 'polushina')

def test_successful_login_user():
    main_page.open_main_page()
    login_page.click_on_login()
    login_page.type_mail()
    login_page.type_password()
# pass

@allure.epic('Login')
@allure.title('Unsuccessful login user')
@allure.link('https://www.litres.ru/', name='litres')
@allure.tag('web')
@allure.severity(Severity.MINOR)
@allure.label('owner', 'polushina')
def test_unsuccessful_login():
    main_page.open_main_page()
    login_page.click_on_login()
    login_page.type_mail()
    login_page.type_wrong_password()
    login_page.verify_error_message()

# pass
import allure
from allure_commons.types import Severity

from litres_shop.pages.UI.main_page import main_page
from litres_shop.pages.UI.my_book_page import read_page


@allure.epic('My book')
@allure.title('Go to My book')
@allure.link('https://www.litres.ru/', name='litres')
@allure.tag('web')
@allure.severity(Severity.MINOR)
@allure.label('owner', 'polushina')
def test_add_book_to_my_book():
    main_page.open_main_page()
    read_page.click_on_my_books()
    read_page.check_my_book()

# pass

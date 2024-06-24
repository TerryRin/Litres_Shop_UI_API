import allure
from allure_commons.types import Severity

from litres_shop.pages.UI.main_page import main_page
from litres_shop.pages.UI.search_page import search_page


@allure.epic('Search')
@allure.title('Search book')
@allure.link('https://www.litres.ru/', name='litres')
@allure.tag('web')
@allure.severity(Severity.MINOR)
@allure.label('owner', 'polushina')
def test_search_book():
    book_name = 'Дюна'
    main_page.open_main_page()
    search_page.find_book_in_search(book_name)
    search_page.check_search_result(book_name)
# pass

@allure.epic('Search')
@allure.title('Search no result')
@allure.link('https://www.litres.ru/', name='litres')
@allure.tag('web')
@allure.severity(Severity.MINOR)
@allure.label('owner', 'polushina')
def test_no_result_search():
    book_name = 'такойкнигинет'
    main_page.open_main_page()
    search_page.find_book_in_search(book_name)
    search_page.check_no_result_search()
# pass

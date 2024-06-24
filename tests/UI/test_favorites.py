import allure
from allure_commons.types import Severity

from litres_shop.pages.UI.favorites_page import favorites_page
from litres_shop.pages.UI.main_page import main_page
from litres_shop.pages.UI.search_page import search_page


@allure.epic('Favorites')
@allure.title('Add book to favorites')
@allure.link('https://www.litres.ru/', name='litres')
@allure.tag('web')
@allure.severity(Severity.MINOR)
@allure.label('owner', 'polushina')
def test_add_book_to_favorites():
    book_name = 'Дюна'
    main_page.open_main_page()
    search_page.find_book_in_search(book_name)
    search_page.check_search_result(book_name)
    search_page.open_search_book(book_name)
    favorites_page.add_book_to_favorites()


# pass

@allure.epic('Favorites')
@allure.title('Go to favorites')
@allure.link('https://www.litres.ru/', name='litres')
@allure.tag('web')
@allure.severity(Severity.MINOR)
@allure.label('owner', 'polushina')
def test_go_to_favorites():
    main_page.open_main_page()
    favorites_page.go_to_favorites()
    favorites_page.verify_favorites()


# pass

@allure.epic('Favorites')
@allure.title('Remove book')
@allure.link('https://www.litres.ru/', name='litres')
@allure.tag('web')
@allure.severity(Severity.MINOR)
@allure.label('owner', 'polushina')
def test_remove_book_to_favorites():
    book_name = 'Дюна'
    main_page.open_main_page()
    search_page.find_book_in_search(book_name)
    search_page.check_search_result(book_name)
    search_page.open_search_book(book_name)
    favorites_page.add_book_to_favorites()
    favorites_page.go_to_favorites()
    favorites_page.verify_favorites()
    favorites_page.open_favorites_book(book_name)
    favorites_page.remove_book_favorites()
# pass

import allure
from selene import browser, have, be


class SearchPage:

    def click_search_page(self, value):
        with allure.step('Клик на поле поиска'):
            browser.element('[data-testid="header__search-form--desktop"]').should(have.text(value))

    def find_book_in_search(self, book_name):
        with allure.step(f'Ввод в поле поиска "{book_name}"'):
            browser.element('[data-testid="search__input"]').type(book_name).press_enter()

    def check_search_result(self, book_name):
        with allure.step('Проверка, что название совпадает'):
            browser.element('[data-testid="art__title"]').should(have.text(book_name))

    def open_search_book(self, book_name):
        with allure.step('Открытие страницы книги'):
            browser.element('[data-testid="art__title"]').should(be.clickable).should(have.text(book_name)).click()

    def check_no_result_search(self):
        with allure.step('Поиск не дал результатов'):
            browser.element('[data-testid="search-title__wrapper"]').should(have.text('ничего не найдено'))


search_page = SearchPage()

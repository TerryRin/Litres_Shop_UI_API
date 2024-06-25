import allure
from selene import browser, have, be, by


class FavoritesPage:
    def add_book_to_favorites(self):
        with (allure.step('Добавление книги в "Отложенное"')):
            browser.element(by.text('Отложить')).should(be.clickable).click()
    def go_to_favorites(self):
        with allure.step('Переход на страницу "Отложенное"'):
            browser.element('[data-testid="tab-favorite"]').click()

    def verify_favorites(self):
        with allure.step('Проверяем, что есть вкладка "Отложенное"'):
            browser.element('[data-testid="navigation__tabItem__label"]').should(have.text('Отложено'))

    def open_favorites_book(self, book_name):
        with allure.step('Открытие страницы отложенной книги'):
            browser.element('[data-testid="art__title"]').should(be.clickable).should(have.text(book_name)).click()

    def remove_book_favorites(self):
        with allure.step('Удаление книг из корзины'):
            browser.element(by.text('Отложить')).should(be.clickable).click()


favorites_page = FavoritesPage()

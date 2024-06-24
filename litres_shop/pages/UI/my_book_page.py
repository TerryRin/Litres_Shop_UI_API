import allure
from selene import browser, have


class ReadPage:

    def click_on_my_books(self):
        with allure.step('Переход в раздел "Мои книги"'):
            browser.element('[data-testid="tab-myBooks"]').click()

    def check_my_book(self):
        with allure.step('Проверяем, что переход в раздел "Мои книги"'):
            browser.element('[data-testid="myBooks__section--wrapper"]').should(have.text('Мои книги'))


read_page = ReadPage()

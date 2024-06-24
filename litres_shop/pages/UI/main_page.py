import allure
from selene import browser


class MainPage:
    def open_main_page(self):
        with allure.step('Открыть главную страницу "Litres"'):
            browser.open('/')

main_page = MainPage()
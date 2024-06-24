import os

import allure
from dotenv import load_dotenv
from selene import browser, have


class LoginPage:
    def click_on_login(self):
        with allure.step('Клик на кнопку "Войти"'):
            browser.element('[data-testid="tab-login"]').click()

    def type_mail(self):
        with allure.step('Ввод почты'):
            load_dotenv()
        mail = os.getenv('USER_EMAIL')
        browser.element('[data-testid="auth__input--enterEmailOrLogin"]').type(mail).press_enter()

    def type_password(self):
        with allure.step('Ввод пароля'):
            load_dotenv()
        password = os.getenv('USER_PASSWORD')
        browser.element('[data-testid="auth__input--enterPassword"]').type(password).press_enter()

    def type_wrong_password(self):
        with allure.step('Ввод пароля с ошибкой'):
            load_dotenv()
        user_password = os.getenv('USER_WRONG_PASSWORD')
        browser.element('[data-testid="auth__input--enterPassword"]').type(user_password).press_enter()

    def verify_error_message(self):
        with allure.step('Проверка вывода ошибки при вводе неверного пароля'):
            browser.element('[data-testid="authorization-popup"]').should(
                have.text('Неверное сочетание логина и пароля'))


login_page = LoginPage()

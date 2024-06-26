<h1> Проект по тестированию веб-сайта "Литрес"</h1>

> <a target="_blank" href="https://www.litres.ru">Ссылка на сайт</a>

![This is an image](images/image/Литрес.png)

<h3> Список проверок, реализованных в автотестах:</h3>

### UI-тесты
- [x] Авторизация пользователя на сайте(успешная и неуспешная)
- [x] Поиск книги (успешный и неуспешный)
- [x] Проверка перехода к разделу "Мои книги"
- [x] Добавление книги в "Отложенное"
- [x] Проверка перехода к разделу "Отложенное"

### API-тесты
- [x] Авторизация пользователя
- [x] Поиск книги (успешный и неуспешный)
- [x] Добавление книги в корзину (успешное и неуспешное)
- [x] Удаление книги из списка "Отложенное"


----
### Используемый стэк:<img src="images/icons/python.png" width="50"><img src="images/icons/allure_report.png" width="50"><img src="images/icons/pytest.png" width="50"><img src="images/icons/allure_testops.png" width="50"><img src="images/icons/selene.png" width="50"><img src="images/icons/intellij_pycharm.png" width="50"><img src="images/icons/jenkins.png" width="50"><img src="images/icons/selenium.png" width="50"><img src="images/icons/selenoid.png" width="50"><img src="images/icons/tg.png" width="50"><img src="images/icons/GitHub.svg" width="50">

----
### Запуск тестов
### Локально
> Для локального запуска с дефолтными значениями необходимо выполнить команду:
```
python -m venv .venv
source .venv/bin/activate
pip install poetry
poetry install --no-root
pytest tests
```

----
### Jenkins
> <a target="_blank" href="https://jenkins.autotests.cloud/job/litres_tests/">Ссылка на проект в Jenkins</a>

#### Для запуска автотестов в Jenkins

1. Открыть <a target="_blank" href="https://jenkins.autotests.cloud/job/litres_tests/">проект</a>
2. Выбрать пункт `Build with Parameters`
3. Нажать кнопку `Build`
4. Результат запуска сборки можно посмотреть в отчёте Allure

----
### Отчеты о прохождении
### Отчет в Allure

#### Общие результаты
![This is an image](images/image/allure_results.png)
#### Пример прохождения теста
![This is an image](images/image/one_test.png)
### Пример видео прохождения ui-автотеста
![This is an gif](images/image/iu_test.gif)


----
### Интеграция с Allure TestOps
#### Пример dashboard с общими результатами тестирования
![This is an image](images/image/dashboard.png)

#### Отчет с результатами запусков
![This is an image](images/image/лаучер.png)

#### Пример отчёта выполнения одного из автотестов
![This is an image](images/image/Test_testOps.png)

----
### Интеграция с Jira

![This is an image](images/image/jira.png)

----
### Оповещения в Telegram
![This is an image](images/image/telegram_bot.png)




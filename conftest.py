'''
1. Создайте GitHub-репозиторий, в котором будут лежать файлы conftest.py и test_items.py.
2. Добавьте в файл conftest.py обработчик, который считывает из командной строки параметр language.
3. Реализуйте в файле conftest.py логику запуска браузера с указанным языком пользователя.
   Браузер должен объявляться в фикстуре browser и передаваться в тест как параметр.
'''

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Добавляем обработку командной строки с параметром language
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help='Choose language: ru, en, fr.. etc')

# Описываем фикстуру объявления браузера, который будет передаваться в тестовый метод как параметр
@pytest.fixture(scope='function')
def browser(request):
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options = options)
    yield browser
    browser.quit()
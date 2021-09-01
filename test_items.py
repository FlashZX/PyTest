'''
4. В файл test_items.py напишите тест, который проверяет, что страница товара на сайте содержит кнопку добавления в корзину.
   Например, можно проверять товар, доступный по http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/.
5. Тест должен запускаться с параметром language следующей командой: pytest --language=es test_items.py
   и проходить успешно. Достаточно, чтобы код работал только для браузера Сhrome.
'''
import time
link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_button_available(browser):
    browser.get(link)
    time.sleep(30)
    # Используем find_elements что бы не падало с исключением если элемент не найден.
    assert browser.find_elements_by_css_selector('.btn-add-to-basket'), 'Элемент не найден!'
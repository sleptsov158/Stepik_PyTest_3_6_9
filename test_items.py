import time


def test_visibility_of_button_add_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(5)
    button = browser.find_elements_by_css_selector(".btn-add-to-basket")
    assert button, "Кнопка 'Добавить в корзину' отсутствует на странице"

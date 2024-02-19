import pytest
import allure
from pages.start_page import StartPage
from conf import MapURLS


@pytest.mark.parametrize("indexes", [
        (0),
        (1)
])
@allure.title("Проверка наличия гиперссылки на страницу 'Данные'")
def test_data_hyperlink_exist(browser, indexes):
    start_page = StartPage(browser)
    start_page.open_start_page()
    assert start_page.Hyperlinks.data_hyperlink_is_displayed(index=indexes), (f"Гиперссылка на данные №{indexes} не отображается")


@pytest.mark.parametrize("indexes", [
        (0),
        (1)
])
@allure.title("Проверка успешного перехода по гиперссылке на страницу 'Данные'")
def test_data_hyperlink_click(browser, indexes):
    start_page = StartPage(browser)
    start_page.open_start_page()
    start_page.Hyperlinks.data_hyperlink_is_displayed(index=indexes)
    start_page.Hyperlinks.data_hyperlink_click(index=indexes)
    start_page.wait_data_page_is_open()
    assert MapURLS.URL_TAB_DATA == browser.current_url, (f"Страница \"Данные\" не открылась")
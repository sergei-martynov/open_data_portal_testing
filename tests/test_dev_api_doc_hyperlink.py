import allure
from pages.start_page import StartPage
from conf import MapURLS


@allure.title("Проверка наличия гиперссылки на документацию API на стартовой странице")
def test_dev_button_exist(browser):
    start_page = StartPage(browser)
    start_page.open_start_page()
    assert start_page.Hyperlinks.dev_api_doc_hyperlink_is_displayed(), (f"Гиперлинк на документацию API не отображается")


@allure.title("Проверка успешного перехода по гиперссылке на документацию API со стартовой страницы")
def test_dev_button_pushed(browser):
    start_page = StartPage(browser)
    start_page.open_start_page()
    start_page.Hyperlinks.dev_api_doc_hyperlink_is_displayed()
    start_page.Hyperlinks.dev_api_doc_hyperlink_click()
    start_page.wait_dev_api_doc_page_is_open()
    assert MapURLS.URL_TAB_DEV_API_DOC == browser.current_url
    assert start_page.make_screenshot("dev_doc_page.png"), (f"Скриншот не сделан")
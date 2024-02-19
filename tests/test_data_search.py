import allure
from pages.data_page import DataPage


@allure.title("Проверка наличия поля 'Поиск' на странице 'Данные'")
def test_search_field_exist(browser):
    data_page = DataPage(browser)
    data_page.open_data_page()
    data_page.wait_page_content()
    data_page.SearchField.search_field_is_displayed
    assert "Поиск..." == data_page.SearchField.search_field_deftext, (f"Поле \"Поиск\" не отображается")


@allure.title("Проверка успешного поиска списка наборов при ручном вводе в поле 'Поиск'")
def test_search_field_main(browser):
    data_page = DataPage(browser)
    data_page.open_data_page()
    data_page.wait_page_content()
    data_page.ValueCounter.count_values_is_displayed
    count_of_values_start = data_page.ValueCounter.count_values_text
    data_page.SearchField.search_field_search(searching_value="ярмарки")
    data_page.ValueCounter.count_values_is_displayed
    count_of_values_end = data_page.ValueCounter.count_values_text
    assert count_of_values_start != count_of_values_end, (f"Поиск списка наборов при ручном вводе не отработал")
import allure
from pages.data_page import DataPage


@allure.title("Проверка наличия поля 'Категории' на странице 'Данные'")
def test_category_exist(browser):
    data_page = DataPage(browser)
    data_page.open_data_page()
    data_page.Category.category_is_displayed
    assert "Категории" == data_page.Category.category_deftext, (f"Dropdown \"Категории\" не отображается")


@allure.title("Проверка отображения категории 'Коммерция' в выпадающем списке")
def test_category_commerce_exist(browser):
    data_page = DataPage(browser)
    data_page.open_data_page()
    data_page.wait_page_content()
    data_page.Category.find_commerce()
    assert data_page.Category.commerce_is_displayed, (f"Категория \"Коммерция\" не отображается")


@allure.title("Проверка функциональности поиска списка наборов данных при выборе категории 'Коммерция'")
def test_category_searching(browser):
    data_page = DataPage(browser)
    data_page.open_data_page()
    data_page.wait_page_content()
    count_of_values_start = data_page.ValueCounter.count_values_text
    data_page.Category.find_commerce()
    data_page.Category.commerce_click()
    data_page.ValueCounter.wait_count_values_text_change(initial_text=count_of_values_start)
    count_of_values_end = data_page.ValueCounter.count_values_text
    assert count_of_values_start != count_of_values_end, (f"Поиск списка наборов при выборе категории не отработал")
import os
import allure
from pages.data_page import DataPage


@allure.title("Проверка наличия кнопки 'Экспорт' на странице 'Данные'")
def test_export_exist(browser):
    data_page = DataPage(browser)
    data_page.open_data_page()
    data_page.wait_page_content()
    assert data_page.ExportBtn.export_btn_is_displayed(index=2), (f"Кнопка \"Экспорт\" не отображается")


@allure.title("Проверка процесса экспорта набора данных")
def test_export_main(browser):
    data_page = DataPage(browser)
    data_page.open_data_page()
    data_page.wait_page_content()
    data_page.ExportBtn.export_btn_is_displayed(index=2)
    data_page.ExportBtn.export_btn_click(index=2)
    data_page.ExportBtn.export_btn_menu_is_displayed
    files_before_download = len(os.listdir(f"{os.getcwd()}/downloads"))
    data_page.ExportBtn.export_btn_download_click(index=5)
    data_page.wait_download(files_before_download=files_before_download)
    assert data_page.wait_download(files_before_download=files_before_download), (f"Файл не скачался")
from pages.base_page import BasePage
from conf import MapURLS, DataSelectors
from selenium.webdriver.common.keys import Keys


class DataPage(BasePage):
    """
    Класс DataPage для работы со страницей "Данные" веб приложения.

    Атрибуты:
    - browser: Экземпляр веб-драйвера.
    - Category: Подкласс, управляющий элементом "Категории" (dropdown) на странице.
    - ValueCounter: Подкласс, управляющий элементом счетчика значений на странице.
    - SearchField: Подкласс, управляющий элементом поля "Поиск" на странице.
    - ExportBtn: Подкласс, управляющий элементами кнопок "Экспорт" на странице.
    """

    def __init__(self, browser):
        super().__init__(browser)
        self.Category = self.Category(browser, self)
        self.ValueCounter = self.ValueCounter(browser, self)
        self.SearchField = self.SearchField(browser, self)
        self.ExportBtn = self.ExportBtn(browser, self)

    def open_data_page(self):
        # Открытие страницы "Данные" веб приложения
        return self.open_page(MapURLS.URL_TAB_DATA)
    
    def wait_page_content(self, selector=DataSelectors.app_loader):
        # Ожидание загрузки контента на странице
        self.wait_for_app_loader_appearance(selector)
        return self.wait_for_app_loader_disappearance(selector)


    class Category(BasePage):
        """
        Подкласс Category предоставляет методы для взаимодействия с элементом "Категории" (dropdown) на странице "Данные".

        Атрибуты:
        - browser: Экземпляр веб-драйвера.
        - data_page: Экземпляр родительского класса DataPage для доступа к его методам.
        """

        def __init__(self, browser, data_page):
            super().__init__(browser)
            self.data_page = data_page

        @property
        def category(self, timeout: int=5):
            # Возвращает кликабельный элемент ввода в поле "Категории"
            return self.wait_to_be_clickable(DataSelectors.category_input, timeout)
        
        def find_commerce(self):
            # Находит и вводит текст 'Торговля' в поле "Категории"
            return self.category.send_keys("Торговля")
    
        def commerce_click(self, timeout=5):
            # Выполняет клик по элементу 'Торговля' в списке категорий
            return self.wait_to_be_clickable(DataSelectors.category_commerce, timeout).click()
        
        @property
        def commerce_is_displayed(self):
            # Проверяет видимость элемента 'Торговля' в списке категорий
            return self.wait_to_be_clickable(DataSelectors.category_commerce, timeout=10).is_displayed()
        
        @property
        def category_deftext(self):
            # Возвращает тайтл поля "Категории"
            return self.find_elements(DataSelectors.category_input_text).text

        @property
        def category_is_displayed(self):
            # Проверяет видимость поля "Категории"
            return self.category.is_displayed()
        

    class ValueCounter(BasePage):
        """
        Подкласс ValueCounter предоставляет методы для взаимодействием с элементом счетчика значений на странице "Данные".

        Атрибуты:
        - browser: Экземпляр веб-драйвера.
        - data_page: Экземпляр родительского класса DataPage для доступа к его методам.
        """

        def __init__(self, browser, data_page):
            super().__init__(browser)
            self.data_page = data_page

        @property
        def count_values(self):
            # Возвращает элемент счетчика значений
            return self.find_elements(DataSelectors.count_values)
    
        @property
        def count_values_is_displayed(self):
            # Проверяет видимость счетчика значений
            return self.count_values.is_displayed()
        
        @property
        def count_values_text(self):
            # Возвращает текст счетчика значений
            return self.count_values.text
    
        def wait_count_values_text_change(self, selector=DataSelectors.count_values, initial_text="", timeout=10):
            # Ожидание изменения текста счетчика значений
            return self.wait_text_until_it_changes(selector, initial_text, timeout)


    class SearchField(BasePage):
        """
        Подкласс SearchField предоставляет методы для взаимодействием с элементом поля "Поиск" на странице "Данные".

        Атрибуты:
        - browser: Экземпляр веб-драйвера.
        - data_page: Экземпляр родительского класса DataPage для доступа к его методам.
        """

        def __init__(self, browser, data_page):
            super().__init__(browser)
            self.data_page = data_page
        
        @property
        def search_field(self, timeout: int=10):
            # Возвращает кликабельное поле "Поиск"
            return self.wait_to_be_clickable(DataSelectors.search_field, timeout)

        @property
        def search_field_is_displayed(self):
            # Проверяет видимость поля "Поиск"
            return self.search_field.is_displayed()

        @property
        def search_field_deftext(self):
            # Возвращает тайтл поля "Поиск"
            return self.find_elements(DataSelectors.search_field).get_attribute("placeholder")

        def search_field_search(self, searching_value):
            # Выполняет поиск значения из 'searching_value'
            search_field = self.find_elements(DataSelectors.search_field)
            search_field.clear()
            search_field.send_keys(searching_value)
            self.wait_for_app_loader_appearance(selector=DataSelectors.search_field_clear_btn)
            search_field.send_keys(Keys.ENTER)
            return self.data_page.wait_page_content(selector=DataSelectors.loader_container)
        

    class ExportBtn(BasePage):
        """
        Подкласс ExportBtn предоставляет методы для взаимодействием с элементами кнопок "Экспорт" на странице "Данные".

        Атрибуты:
        - browser: Экземпляр веб-драйвера.
        - data_page: Экземпляр родительского класса DataPage для доступа к его методам.
        """

        def __init__(self, browser, data_page):
            super().__init__(browser)
            self.data_page = data_page

        def export_btn(self, index: int=0):
            # Возвращает элемент искомой кнопоки "Экспорт" по её индексу
            return self.find_elements(DataSelectors.export_btn, index)
        
        def export_btn_download(self, index: int=0):
            # Возвращает элемент искомой кнопоки формата экспорта по её индесу
            return self.find_elements(DataSelectors.export_btn_download, index)
        
        @property
        def export_btn_menu_is_displayed(self, timeout: int=0):
            # Проверяет видимость меню кнопок форматов экспорта
            self.wait_for_app_loader_appearance(DataSelectors.export_btn_menu, timeout)
            return self.find_elements(DataSelectors.export_btn_menu).is_displayed()
        
        def export_btn_is_displayed(self, index: int=0):
            # Проверяет видимость кнопоки формата экспорта по её индексу
            return self.export_btn(index).is_displayed()

        def export_btn_click(self, index: int=0):
            # Выполняет нажатие по искомой кнопке "Экспорт", по её индексу
            return self.export_btn(index).click()
            
        def export_btn_download_click(self, index: int=0):
            # Выполняет нажатие по кнопке необходимого формата экспорта по её индесу
            return self.export_btn_download(index).click()

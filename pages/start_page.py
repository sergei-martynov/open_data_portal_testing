from pages.base_page import BasePage
from conf import MapURLS, DataSelectors, DevSelectors


class StartPage(BasePage):
    """
    Класс StartPage для работы со стартовой страницей веб приложения.

    Атрибуты:
    - browser: Экземпляр веб-драйвера, предоставляющий доступ к браузеру.
    - Hyperlinks: Подкласс, управляющий гиперссылками на странице.
    """

    def __init__(self, browser):
        super().__init__(browser)
        self.Hyperlinks = self.Hyperlinks(browser, self)


    def open_start_page(self):
        # Открывает главную страницу приложения
        return self.open_page(MapURLS.URL_MAIN_PAGE)
    
    
    def wait_data_page_is_open(self, timeout: int=5):
        # Ожидает открытия страницы с данными в течение указанного времени
        return self.is_opened(MapURLS.URL_TAB_DATA, timeout)
    

    def wait_dev_api_doc_page_is_open(self, timeout: int=5):
        # Ожидает открытия страницы с документацией API в течение указанного времени
        return self.is_opened(MapURLS.URL_TAB_DEV_API_DOC, timeout)
    

    class Hyperlinks(BasePage):
        """
        Подкласс Hyperlinks предоставляет методы для взаимодействия с гиперссылками на странице.

        Атрибуты:
        - browser: Экземпляр веб-драйвера.
        - start_page: Экземпляр родительского класса StartPage для доступа к его методам.
        """

        def __init__(self, browser, start_page):
            super().__init__(browser)
            self.start_page = start_page
        
        def data_hyperlink(self, index: int=0):
            # Возвращает элемент гиперссылки на страницу с данными
            return self.find_elements(DataSelectors.data_hyperlink, index)
        

        def data_hyperlink_is_displayed(self, index: int=0):
            # Проверяет видимость гиперссылки на страницу с данными
            return self.data_hyperlink(index).is_displayed()
        
        
        def data_hyperlink_click(self, index: int=0):
            # Выполняет нажатие по гиперссылке на стринцу с данными
            return self.data_hyperlink(index).click()
        

        def dev_api_doc_hyperlink(self, index: int=0):
            # Возвращает элемент гиперссылки на страницу с API документацией
            return self.find_elements(DevSelectors.dev_hyperlink, index)
        

        def dev_api_doc_hyperlink_is_displayed(self, index: int=0):
            # Проверяет видимость гиперссылки на страницу с API документацией
            return self.dev_api_doc_hyperlink(index).is_displayed()
        
        
        def dev_api_doc_hyperlink_click(self, index: int=0):
            # Выполняет нажатие по гиперссылке на страницу с API документацией
            return self.dev_api_doc_hyperlink(index).click()
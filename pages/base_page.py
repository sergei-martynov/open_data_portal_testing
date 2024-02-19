import os
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from conf import GlobalVariables


class BasePage():
    """
    Базовый класс, предоставляющий основные функциональности для всех страниц веб приложения.

    Атрибуты:
    - _browser: Экземпляр веб-драйвера, предоставляющий доступ к браузеру.
    """

    def __init__(self, browser):
        self._browser = browser

    def open_page(self, url):
        # Открывает страницу веб приложения по переданному URL
        return self._browser.get(url)
    
    
    def is_opened(self, url, timeout):
        # Проверка открытия страницы по URL с использованием явных ожиданий
        try:
            WebDriverWait(self._browser, timeout).until(
                EC.url_to_be(url)
            )
            return True
        except:
            return False, (f"Страница - {url}, не отобразилась")
    

    def find_elements(self, selector, index=None):
        # Поиск элемента(ов) на странице по переданному селектору
        elements = self._browser.find_elements(*selector)

        if not elements:
            raise NoSuchElementException("Элемент не найден")
        
        if index is not None:
            # Если указан индекс, возвращаем элемент по индексу
            if 0 <= index < len(elements):
                return elements[index]
            else:
                raise IndexError(f"Индекс выходит за пределы списка элементов. Всего элементов {len(elements)}")
        else:
            if len(elements) > 1:
                raise Exception(f"Найден список элементов. Укажите индекс значения. Всего элементов {len(elements)}")
            return elements[0]


    def wait_to_be_clickable(self, selector, timeout: int=5):
        # Ожидание, пока элемент станет кликабельным, с использованием явных ожиданий
        try:
            element = WebDriverWait(self._browser, timeout).until(
                EC.element_to_be_clickable(selector)
            )
            return element
        except:
            raise Exception(f"Элемент не кликабелен - {selector}")
        

    def wait_for_app_loader_appearance(self, selector, timeout: int=5):
        # Ожидание появления элемента с использованием явных ожиданий
        try:
            element = WebDriverWait(self._browser, timeout).until(
                EC.presence_of_element_located(selector)
            )
            return element
        except TimeoutException:
            return TimeoutException(f"Элемент \"{selector}\" не появился в течение {timeout} секунд")
    

    def wait_for_app_loader_disappearance(self, selector, timeout: int=5):
        # Ожидание исчезновения элемента с использованием явных ожиданий
        try:
            element = WebDriverWait(self._browser, timeout).until(
                EC.invisibility_of_element_located(selector)
            )
            return element
        except TimeoutException:
            return TimeoutException(f"Элемент \"{selector}\" не исчез в течение {timeout} секунд")

    
    def wait_text_until_it_changes(self, selector, initial_text, timeout: int=10):
        # Ожидание изменения текста элемента с использованием явных ожиданий
        try:
            element = WebDriverWait(self._browser, timeout).until_not(
                EC.text_to_be_present_in_element(selector, initial_text)
            )
            return element
        except TimeoutException as e:
            raise Exception(f"Элемент {selector} не изменился. Ошибка: {e}")

    
    def make_screenshot(self, file_name):
        # Создание скриншота страницы и сохранение его в указанной директории
        screenshots_directory = os.path.join(os.getcwd(), "screenshots")

        # Проверка существования директории, и создание ее, если она отсутствует
        if not os.path.exists(screenshots_directory):
            os.makedirs(screenshots_directory)

        screenshot_path = os.path.join(screenshots_directory, file_name)

        try:
            return self._browser.save_screenshot(screenshot_path)
        except Exception as e:
            raise Exception(f"Ошибка при создании скриншота: {e}")
        

    def wait_download(self, files_before_download: int, timeout: int=30):
        # Ожидание завершения загрузки файлов в указанную директорию
        try:
            WebDriverWait(self._browser, timeout).until(
                lambda _: len(os.listdir(GlobalVariables.download_dir_path)) > files_before_download
            )
            return True
        except TimeoutException:
            assert False, (f"Файл не скачался в течение {timeout} секунд. Пожалуйста, проверьте директорию загрузки")
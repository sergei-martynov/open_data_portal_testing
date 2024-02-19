import os
import pytest
from selenium import webdriver
from conf import GlobalVariables


def create_chrome_options():
    chrome_options = webdriver.ChromeOptions()
    download_directory = os.path.join(os.getcwd(), "downloads")
    prefs = {
        "download.default_directory": download_directory,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    }
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.page_load_strategy = "normal" #eager none
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--window-size=1900,1080")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
    return chrome_options

def create_firefox_options():
    firefox_options = webdriver.FirefoxOptions()
    download_directory = os.path.join(os.getcwd(), "downloads")
    firefox_options.add_argument("--width=1900")
    firefox_options.add_argument("--height=1080")
    firefox_options.add_argument("--headless")
    firefox_options.add_argument("--no-sandbox")
    firefox_options.page_load_strategy = "normal" #eager none
    firefox_options.set_preference("browser.download.folderList", 2)
    firefox_options.set_preference("browser.download.dir", download_directory)
    firefox_options.set_preference("browser.download.useDownloadDir", True)
    firefox_options.set_preference("browser.helperApps.neverAsk.saveToDisk", "")
    return firefox_options


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox", help="Укажите браузер для запуска тестов (chrome или firefox)")


@pytest.fixture
def creating_download_directory():
    if not os.path.exists(GlobalVariables.download_dir_path):
        return os.makedirs(GlobalVariables.download_dir_path)


@pytest.fixture
def browser(request, creating_download_directory):
    selected_browser = request.config.getoption("--browser").lower()
    
    if selected_browser == "chrome":
        options = create_chrome_options()
        browser = webdriver.Chrome(options=options)
    elif selected_browser == "firefox":
        options = create_firefox_options()
        browser = webdriver.Firefox(options=options)
    else:
        raise ValueError(f"Браузер {selected_browser} не поддерживается")

    yield browser
    browser.quit()
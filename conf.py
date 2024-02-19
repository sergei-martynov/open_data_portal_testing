import os


class MapURLS:
    URL_MAIN_PAGE = "https://data.mos.ru"
    URL_TAB_DATA = "https://data.mos.ru/opendata"
    URL_TAB_DEV = "https://data.mos.ru/developers"
    URL_TAB_DEV_API_DOC = "https://data.mos.ru/developers/documentation"
    

class DataSelectors:
    app_loader = ("xpath", '//app-loader')
    loader_container = ("xpath", '//div[@class="loader-container"]')
    header_is_disable = ("xpath", 'class="wrapper table-edge-margin ng-star-inserted disable"')
        
    page_error_message = ("xpath", '//app-error-page-message')

    data_hyperlink = ("xpath", '//a[@class="transition-container td-n" and @href="/opendata"]')
    
    category_input_text = ("xpath", '//div[contains(@class, "input-wrapper")]//span[contains(text(), "Категории")]')
    category_input = ("xpath", '(//div[@class="input-wrapper ng-star-inserted"]/input)[1]')
    category_commerce = ("xpath", '//label//span[contains(text(), "Торговля")]')
    
    count_values = ("xpath", '//span[contains(@class, "text-count")]')

    search_field = ("xpath", '//input[contains(@class, "search-input")]')
    search_field_search_btn = ("xpath", '//button[contains(@class, "search-btn") and not(contains(@class, "js-clear"))]')
    search_field_clear_btn = ("xpath", '//button[contains(@class, "js-clear ng-star-inserted")]')
    search_field_category = ("xpath", '//span-category[contains(@class, "category-name")]')
    search_field_manual_search = ("xpath", '//div[@class="title-container"]//span[contains(text(), "ярмарки")]')
    
    export_btn = ("xpath", '(//app-download-button//button)')
    export_btn_menu = ("xpath", '//div[contains(@id, "mat-menu-panel-")]')
    export_btn_download = ("xpath", '(//div[contains(@id, "mat-menu-panel-")]//button)')


class DevSelectors:
    dev_hyperlink = ("xpath", '//a[@class="transition-container td-n" and @href="/developers/documentation"]')


class GlobalVariables:
    download_dir_path = os.path.join(os.getcwd(), "downloads")
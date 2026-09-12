import allure
from pages.main_page import MainPage
from data.urls import SCOOTER_URL


@allure.epic("Главная страница")
@allure.feature("Логотипы")
class TestLogo:

    @allure.title("Логотип Самоката ведёт на главную")
    def test_scooter_logo_opens_main(self, driver):
        page = MainPage(driver)
        page.open_main()
        page.click_order_header()
        page.click_scooter_logo()
        assert page.current_url().rstrip("/") == SCOOTER_URL.rstrip("/")

    @allure.title("Логотип Яндекса открывает Дзен в новом окне")
    def test_yandex_logo_opens_dzen(self, driver):
        page = MainPage(driver)
        page.open_main()
        page.click_yandex_logo()
        page.switch_to_new_window()
        page.wait_url_loaded()
        url = page.current_url()
        assert "dzen.ru" in url or "ya.ru" in url or "yandex.ru" in url

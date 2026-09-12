import allure
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data.order_data import ORDER_DATA


@allure.epic("Оформление заказа")
@allure.feature("Позитивный сценарий")
class TestOrder:

    def _make_order(self, driver, order):
        page = OrderPage(driver)
        page.fill_who_is_the_scooter_for(
            order["name"],
            order["surname"],
            order["address"],
            order["metro"],
            order["phone"],
        )
        page.fill_rent_info(
            order["date"],
            order["period"],
            order["color"],
            order["comment"],
        )
        assert "Заказ оформлен" in page.success_text()

    @allure.title("Заказ самоката через кнопку в шапке")
    @pytest.mark.parametrize("order", [ORDER_DATA[0]])
    def test_order_from_header(self, driver, order):
        main = MainPage(driver)
        main.open_main()
        main.click_order_header()
        self._make_order(driver, order)

    @allure.title("Заказ самоката через кнопку внизу")
    @pytest.mark.parametrize("order", [ORDER_DATA[1]])
    def test_order_from_footer(self, driver, order):
        main = MainPage(driver)
        main.open_main()
        main.click_order_footer()
        self._make_order(driver, order)
        
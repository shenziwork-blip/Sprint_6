import allure
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data.order_data import ORDER_DATA


@allure.epic("Оформление заказа")
@allure.feature("Позитивный сценарий")
class TestOrder:

    @allure.title("Заказ самоката через кнопку {button}")
    @pytest.mark.parametrize(
        "button, order",
        [
            ("header", ORDER_DATA[0]),
            ("footer", ORDER_DATA[1]),
        ],
    )
    def test_successful_order(self, driver, button, order):
        main = MainPage(driver)
        main.open_main()

        if button == "header":
            main.click_order_header()
        else:
            main.click_order_footer()

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
        
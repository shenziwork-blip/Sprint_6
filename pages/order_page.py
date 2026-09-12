import allure
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):
    @allure.step("Заполнить форму «Для кого самокат»")
    def fill_who_is_the_scooter_for(self, name, surname, address, metro, phone):
        self.type(OrderPageLocators.NAME, name)
        self.type(OrderPageLocators.SURNAME, surname)
        self.type(OrderPageLocators.ADDRESS, address)

        metro_field = self.scroll_to(OrderPageLocators.METRO)
        metro_field.click()
        metro_field.send_keys(metro)
        metro_field.send_keys(Keys.ARROW_DOWN)
        metro_field.send_keys(Keys.ENTER)
        metro_field.send_keys(Keys.ESCAPE)
        self.scroll_to(OrderPageLocators.PHONE)
        self.type(OrderPageLocators.PHONE, phone)
        self.click(OrderPageLocators.NEXT_BUTTON)
        self.scroll_to(OrderPageLocators.DATE)

    @allure.step("Заполнить «Про аренду» и подтвердить заказ")
    def fill_rent_info(self, date, period, color, comment):
        date_field = self.scroll_to(OrderPageLocators.DATE)
        date_field.click()
        date_field.send_keys(date)
        date_field.send_keys(Keys.ENTER)
        date_field.send_keys(Keys.ESCAPE)

        self.click_native(OrderPageLocators.PERIOD_DROPDOWN)
        option = (
            OrderPageLocators.PERIOD_OPTION[0],
            OrderPageLocators.PERIOD_OPTION[1].format(period),
        )
        self.click_native(option)

        if color == "black":
            self.click(OrderPageLocators.COLOR_BLACK)
        elif color == "grey":
            self.click(OrderPageLocators.COLOR_GREY)

        self.type(OrderPageLocators.COMMENT, comment)
        self.click(OrderPageLocators.ORDER_BUTTON)
        self.click(OrderPageLocators.CONFIRM_BUTTON)

    def success_text(self):
        return self.get_text(OrderPageLocators.SUCCESS_MODAL)
    
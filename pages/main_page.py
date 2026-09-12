import allure
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from data.urls import SCOOTER_URL


class MainPage(BasePage):
    @allure.step("Открыть главную страницу")
    def open_main(self):
        self.open(SCOOTER_URL)
        self.accept_cookies()

    def accept_cookies(self):
        try:
            self.click(MainPageLocators.COOKIE_BUTTON)
        except TimeoutException:
            pass

    @allure.step("Нажать «Заказать» в шапке")
    def click_order_header(self):
        self.click(MainPageLocators.ORDER_BUTTON_HEADER)

    @allure.step("Нажать «Заказать» внизу страницы")
    def click_order_footer(self):
        self.scroll_to(MainPageLocators.ORDER_BUTTON_FOOTER)
        self.click(MainPageLocators.ORDER_BUTTON_FOOTER)

    @allure.step("Кликнуть логотип Самоката")
    def click_scooter_logo(self):
        self.click(MainPageLocators.LOGO_SCOOTER)

    @allure.step("Кликнуть логотип Яндекса")
    def click_yandex_logo(self):
        self.click(MainPageLocators.LOGO_YANDEX)

    @allure.step("Открыть вопрос FAQ {index}")
    def open_faq(self, index):
        question = (
            MainPageLocators.FAQ_QUESTION[0],
            MainPageLocators.FAQ_QUESTION[1].format(index),
        )
        self.scroll_to(question)
        self.click(question)

    def get_faq_answer(self, index):
        answer = (
            MainPageLocators.FAQ_ANSWER[0],
            MainPageLocators.FAQ_ANSWER[1].format(index),
        )
        return self.get_text(answer)
    
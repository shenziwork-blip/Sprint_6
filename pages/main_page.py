from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from data.urls import SCOOTER_URL
from selenium.common.exceptions import TimeoutException

class MainPage(BasePage):
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")
    ORDER_BUTTON_HEADER = (By.XPATH, "//div[contains(@class,'Header_Nav')]//button[text()='Заказать']",)
    ORDER_BUTTON_FOOTER = (By.XPATH, "//div[contains(@class,'Home_FinishButton')]//button[text()='Заказать']",)
    LOGO_SCOOTER = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    LOGO_YANDEX = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")
    FAQ_QUESTION = (By.ID, "accordion__heading-{}")
    FAQ_ANSWER = (By.ID, "accordion__panel-{}")

    def open_main(self):
        self.open(SCOOTER_URL)
        self.accept_cookies()

    def accept_cookies(self):
        try:
            self.click(self.COOKIE_BUTTON)
        except TimeoutException: pass

    def click_order_header(self):
        self.click(self.ORDER_BUTTON_HEADER)

    def click_order_footer(self):
        self.scroll_to(self.ORDER_BUTTON_FOOTER)
        self.click(self.ORDER_BUTTON_FOOTER)

    def click_scooter_logo(self):
        self.click(self.LOGO_SCOOTER)

    def click_yandex_logo(self):
        self.click(self.LOGO_YANDEX)

    def open_faq(self, index):
        question = (self.FAQ_QUESTION[0], self.FAQ_QUESTION[1].format(index))
        self.scroll_to(question)
        self.click(question)

    def get_faq_answer(self, index):
        answer = (self.FAQ_ANSWER[0], self.FAQ_ANSWER[1].format(index))
        return self.get_text(answer)
    
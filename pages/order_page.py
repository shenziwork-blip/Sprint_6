from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage


class OrderPage(BasePage):
    NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[contains(text(),'Далее')]")
    DATE = (By.XPATH, "//input[contains(@placeholder,'Когда привезти')]")
    COLOR_BLACK = (By.ID, "black")
    COLOR_GREY = (By.ID, "grey")
    COMMENT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//div[contains(@class,'Order_Buttons')]//button[text()='Заказать']",)
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Да']")
    SUCCESS_MODAL = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")

    def fill_who_is_the_scooter_for(self, name, surname, address, metro, phone):
        self.type(self.NAME, name)
        self.type(self.SURNAME, surname)
        self.type(self.ADDRESS, address)

        metro_field = self.scroll_to(self.METRO)
        metro_field.click()
        metro_field.send_keys(metro)
        metro_field.send_keys(Keys.ARROW_DOWN)
        metro_field.send_keys(Keys.ENTER)

        self.type(self.PHONE, phone)
        self.click(self.NEXT_BUTTON)
        self.scroll_to(self.DATE)

    def fill_rent_info(self, date, period, color, comment):
        date_field = self.scroll_to(self.DATE)
        date_field.click()
        date_field.send_keys(date)
        date_field.send_keys(Keys.ENTER)
        date_field.send_keys(Keys.ESCAPE)

        self.click_native((By.CLASS_NAME, "Dropdown-control"))
        self.click_native((By.XPATH, f"//div[@class='Dropdown-option' and text()='{period}']"))

        if color == "black":
            self.click(self.COLOR_BLACK)
        elif color == "grey":
            self.click(self.COLOR_GREY)

        self.type(self.COMMENT, comment)
        self.click(self.ORDER_BUTTON)
        self.click(self.CONFIRM_BUTTON)

    def success_text(self):
        return self.get_text(self.SUCCESS_MODAL)
    
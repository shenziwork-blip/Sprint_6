from selenium.webdriver.common.by import By


class MainPageLocators:
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")
    ORDER_BUTTON_HEADER = (
        By.XPATH,
        "//div[contains(@class,'Header_Nav')]//button[text()='Заказать']",
    )
    ORDER_BUTTON_FOOTER = (
        By.XPATH,
        "//div[contains(@class,'Home_FinishButton')]//button[text()='Заказать']",
    )
    LOGO_SCOOTER = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    LOGO_YANDEX = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")
    FAQ_QUESTION = (By.ID, "accordion__heading-{}")
    FAQ_ANSWER = (By.ID, "accordion__panel-{}")
    
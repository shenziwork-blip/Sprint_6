import allure
import pytest
from pages.main_page import MainPage
from data.order_data import FAQ_DATA


@allure.epic("Главная страница")
@allure.feature("Вопросы о важном")
class TestFaq:

    @allure.title("Открывается ответ на вопрос FAQ")
    @allure.description("При клике на вопрос отображается соответствующий текст ответа")
    @pytest.mark.parametrize("index, expected_text", FAQ_DATA)
    def test_faq_answer_opens(self, driver, index, expected_text):
        page = MainPage(driver)
        page.open_main()
        page.open_faq(index)
        assert page.get_faq_answer(index) == expected_text
        
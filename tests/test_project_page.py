import allure
from allure_commons.types import Severity
from selene import browser, command, have, be, by

from QAguru_20_homework_14.page import ProjectPage

project_page = ProjectPage()


@allure.tag("web")
@allure.label("owner", "Anna Krasnokutskaia")
@allure.feature("Проверяем основные разделы главной страницы")
@allure.story('По кнопке "О продукте" мы переходим в соответствующий раздел')
@allure.severity(Severity.CRITICAL)
def test_product_button():
    project_page.open_page()
    project_page.click_button_from_menu("О продукте")
    project_page.product_button_result().should(have.text("О продукте"))


@allure.tag("web")
@allure.label("owner", "Anna Krasnokutskaia")
@allure.feature("Проверяем основные разделы главной страницы")
@allure.story('По кнопке "Особенности" мы переходим в соответствующий раздел')
@allure.severity(Severity.CRITICAL)
def test_feature_button():
    project_page.open_page()
    project_page.click_button_from_menu("Особенности")
    project_page.feature_button_result().should(have.text("Особенности KeyStack"))


@allure.tag("web")
@allure.label("owner", "Anna Krasnokutskaia")
@allure.feature("Проверяем основные разделы главной страницы")
@allure.story('По кнопке "Преимущества" мы переходим в соответствующий раздел')
@allure.severity(Severity.CRITICAL)
def test_advantages_button():
    project_page.open_page()
    project_page.click_button_from_menu("Преимущества")
    project_page.advantages_button_result().should(have.text("Преимущества"))


@allure.tag("web")
@allure.label("owner", "Anna Krasnokutskaia")
@allure.feature("Проверяем основные разделы главной страницы")
@allure.story('По кнопке "Обучение и поддержка" мы переходим в соответствующий раздел')
@allure.severity(Severity.CRITICAL)
def test_training_button():
    project_page.open_page()
    project_page.click_button_from_menu("Обучение и поддержка")
    project_page.training_button_result().should(have.text("Про обучение и поддержку"))


@allure.tag("web")
@allure.label("owner", "Anna Krasnokutskaia")
@allure.feature("Проверяем работу кнопки смены языка")
@allure.story('По кнопке "Eng" на странице присутствует текст на английском языке')
@allure.severity(Severity.CRITICAL)
def test_eng_button():
    project_page.open_page()
    project_page.click_eng_button()
    project_page.eng_button_result().should(have.text("Cloud platform"))


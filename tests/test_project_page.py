import allure
from selene import browser, command, have, be, by
from QAguru_20_homework_14.moodel import Gender, Hobby, State, User
from QAguru_20_homework_14.page import ProjectPage

project_page = ProjectPage()

def test_product_button():
    project_page.open_page()
    project_page.click_button("О продукте")
    project_page.product_button_result().should(have.text("О продукте"))

def test_feature_button():
    project_page.open_page()
    project_page.click_button("Особенности")
    project_page.feature_button_result().should(have.text("Особенности KeyStack"))

def test_advantages_button():
    project_page.open_page()
    project_page.click_button("Преимущества")
    project_page.advantages_button_result().should(have.text("Преимущества"))
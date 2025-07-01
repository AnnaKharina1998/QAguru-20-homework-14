import allure
from selene import browser, command, have, be, by

from QAguru_20_homework_14.moodel import User
from QAguru_20_homework_14.resourses import resource_path


class ProjectPage:
    def open_page(self):
        browser.open("https://keystack.ru/")

    def click_button(self, button_name):
        browser.element(by.xpath(f"//header/descendant-or-self::nav/ul[@class='main-menu']/li/a[text()='{button_name}']")).click()


    def product_button_result(self):
        return browser.element(by.xpath('//section[@id="product"]/descendant-or-self::h2[@class="section-title"]'))

    def feature_button_result(self):
        return browser.element(by.xpath('//section[@id="features"]/descendant-or-self::h2[@class="section-title alCenter"]'))

    def advantages_button_result(self):
        return browser.element(by.xpath('//section[@id="advantages"]/descendant-or-self::h2[@class="section-title"]'))


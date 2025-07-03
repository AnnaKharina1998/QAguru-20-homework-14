import allure
from selene import browser, command, have, be, by

class ProjectPage:
    def open_page(self):
        with allure.step("Открыть страницу проекта"):
            browser.open("https://keystack.ru/")

    def click_button_from_menu(self, button_name):
        with allure.step(f'Нажать кнопку "{button_name}"'):
            browser.element(by.xpath(f"//header/descendant-or-self::nav/ul[@class='main-menu']/li/a[text()='{button_name}']")).click()


    def product_button_result(self):
        with allure.step("Результат нажатия на кнопку"):
            return browser.element(by.xpath('//section[@id="product"]/descendant-or-self::h2[@class="section-title"]'))

    def feature_button_result(self):
        with allure.step("Результат нажатия на кнопку"):
            return browser.element(by.xpath('//section[@id="features"]/descendant-or-self::h2[@class="section-title alCenter"]'))

    def advantages_button_result(self):
        with allure.step("Результат нажатия на кнопку"):
            return browser.element(by.xpath('//section[@id="advantages"]/descendant-or-self::h2[@class="section-title"]'))

    def training_button_result(self):
        with allure.step("Результат нажатия на кнопку"):
            return browser.element(by.xpath('//section[@id="training"]/descendant-or-self::h2[@class="section-title"]'))

    def click_eng_button(self):
        with allure.step(f'Нажать кнопку "Eng"'):
            browser.element(by.text("Eng")).click()

    def eng_button_result(self):
        with allure.step("Результат нажатия на кнопку"):
            return browser.element(by.xpath('//h1[@class="page-title"]'))
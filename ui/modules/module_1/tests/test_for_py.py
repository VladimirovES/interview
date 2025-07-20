import allure

import faker

from ui.base_test_ui import BaseTestUI

fake = faker.Faker()


@allure.story('SomeSuite')
class TestHello(BaseTestUI):

    @allure.title('this Title')
    def test_example(self):
        #Arrange
        text = fake.text()

        #Act
        self.main_page.open()
        self.main_page.search_input.fill(text=text)

        #Assert


    def test_example_2(self):
        self.main_page.open(url='https://google.com')
        self.main_page.search_input.fill(text='hohoh')

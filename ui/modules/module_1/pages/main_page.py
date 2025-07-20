from ui.components.input import Input
from ui.base.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.search_input = Input(locator="//textarea[@name='q']", name='Поиск', page=page)
        # self.choose = Select(locator="//select[@name='c']", name='<UNK>', page=page)


    def open(self, url="https://google.com"):
        super().open(url)
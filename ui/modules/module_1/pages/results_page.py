from ui.base.base_page import BasePage


class Button:
    ...

class ResultsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.first_var = Button()
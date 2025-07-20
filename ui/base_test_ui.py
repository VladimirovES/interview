import pytest

from ui.modules.module_1.pages.main_page import MainPage


class BaseTestUI:
    main_page: MainPage

    @pytest.fixture(autouse=True)
    def setup_pages(self, page, request):
        request.cls.main_page = MainPage(page)
        # request.cls.boy_page = Buy(browser)

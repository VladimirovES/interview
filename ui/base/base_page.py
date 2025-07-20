import allure
from playwright.sync_api import Page

from playwright.sync_api import expect


class BasePage:

    def __init__(self, page: Page):
        self._page = page

    def open(self, url: str):
        with allure.step(f'Open page {url}'):
            self._page.goto(url, wait_until='domcontentloaded')

    def close(self):
        ...

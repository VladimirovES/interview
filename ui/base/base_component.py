from abc import ABC, abstractmethod

import allure
from playwright.sync_api import Page


class Component(ABC):
    def __init__(self, page: Page, locator: str, name: str):
        self.page = page
        self.locator = locator
        self.name = name

    @property
    @abstractmethod
    def type_of(self):
        return 'component'

    def _format_locator(self, **kwargs):
        return self.locator.format(**kwargs)

    def _find_element(self, **kwargs):
        return self.page.locator(self._format_locator(**kwargs))

    def click(self, **kwargs):
        with allure.step(f'Click on {self.type_of} with name {self.name}'):
            self._find_element(**kwargs).click()



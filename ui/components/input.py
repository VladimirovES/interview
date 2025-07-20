import allure

from ui.base.base_component import Component


class Input(Component):

    @property
    def type_of(self):
        return 'input'

    def fill(self, text: str, **kwargs):
        with allure.step(f'{self.type_of} {self.name} fill {text} '):
            self._find_element(**kwargs).fill(value=text)


import pytest
from playwright.sync_api import Page, expect
from pydantic import BaseModel, Field

from faker import Faker

fake = Faker()

#
# @pytest.fixture(scope='function')
# def page():
#     with sync_playwright() as playwright:
#         chromium = playwright.chromium.launch(headless=False)
#         yield chromium.new_context().new_page()
#         chromium.close()


class AuthData(BaseModel):
    login: str = Field(default_factory=lambda x: fake.email())
    password: str = Field(default_factory=lambda x: fake.password())


class SomePage:
    def __init__(self, page: Page):
        self.page = page
        self.login = page.locator("input[type=text]")
        self.password = page.locator("input[type=text]")
        self.submit = page.locator("input[type=text]")

        self.one_more = page.locator("input[type=text]")

    def authenticate(self, auth_data: AuthData):
        self.login.fill(value=auth_data.login)
        self.password.fill(value=auth_data.password)
        self.submit.click()
        return self

    def check_fields(self):
        self.one_more.click()


class SecondPage:
    def __init__(self, page: Page):
        self.page = page
        self.login = page.locator("input[type=text]")
        self.password = page.locator("input[type=text]")
        self.submit = page.locator("input[type=text]")

    def check_this_think(self): ...


def handle_request(request):
    print(f"Request: {request.method} {request.url}")


def test_ssss(page: Page):
    #Arrange
    price = 10000

    page.on("request",handle_request )

    #Act

    page.goto("https://demoqa.com/")
    page.locator("//div[@class='card mt-4 top-card' and .//h5[text()='Elements']]").click()
    page.locator("//li[@id='item-3' and .//span[text()='Web Tables']]").click()

    #Arrange
    expect(page.locator("(//div[contains(@class, 'rt-tr -')])[1]/div[text()='{price}']".format(price=10000))).to_have_text("10000", timeout=2000)
    expect(page.locator("#edit-record-2")).to_be_visible()

    # (SomePage(page)
    #  .authenticate(AuthData())
    #  )

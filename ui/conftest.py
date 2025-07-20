import pytest
from playwright.sync_api import sync_playwright



@pytest.fixture(scope='session')
def browser(request):
    with sync_playwright() as playwright:
        headless = request.config.getoption("--headless")
        browser = playwright.chromium.launch(headless=headless)
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()




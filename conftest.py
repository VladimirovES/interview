def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chromium",
                     help='Браузер для запуска тестов')
    parser.addoption('--headless', action='store_true', default=False)
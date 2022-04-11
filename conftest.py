import pytest

from selenium import webdriver


def pytest_addoption(parser: pytest.Parser):
    parser.addoption("--browser", action="store", default='chrome')
    parser.addoption("--executor", action="store", default='192.168.0.105')
    # parser.addoption("--executor", action="store", default='10.8.38.47')


@pytest.fixture(scope="function")
def browser(request):
    browser = request.config.getoption("--browser")
    executor = request.config.getoption("--executor")
    capabilities = {
        "browserName": browser,
        "browserVersion": "101.0",
        "selenoid:options": {
            "enableVNC": False,
            "enableVideo": False
        }
    }
    browser = webdriver.Remote(command_executor=f'http://{executor}:4444/wd/hub',
                               desired_capabilities=capabilities)
    # browser.implicitly_wait(10)
    # browser.maximize_window()

    yield browser
    browser.quit()

from selenium.webdriver.chrome.options import Options
import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Выберите язык интерфейса, например: es или ru")
    parser.addoption('--browser', action='store', default='chrome')
    parser.addoption('--executor', action='store', default='10.8.80.18')
    # parser.addoption('--executor', action='store', default='192.168.0.103')


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("--language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})

    # browser = webdriver.Chrome(options=options)
    browser = request.config.getoption("--browser")
    executor = request.config.getoption("--executor")

    capabilities = {
        "BrowserName": browser
    }
    driver = webdriver.Remote(
        command_executor=f"http://{executor}:4444/wd/hub",
        desired_capabilities=capabilities
    )

    yield driver
    driver.quit()

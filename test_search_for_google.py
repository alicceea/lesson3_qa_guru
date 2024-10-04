from webbrowser import Chrome

import pytest
from selenium.webdriver import Firefox, FirefoxOptions, Chrome
from selene import browser, be, have
from selene.support.shared import config
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def configure_browser(scope="session"):
    print("Браузер")
    config.browser_name = 'firefox'
    config.base_url = 'https://google.com'
    config.timeout = 10

    yield

    print("Закрываем браузер")


@pytest.fixture
def configure_browser_options(configure_browser):
    options = FirefoxOptions()
    options.add_argument("--width=1920")
    options.add_argument("--height=1080")
    options.timeouts = {'pageLoad': 3000}
    options.page_load_strategy = 'none'
    browser.config.driver_options = options


def test_search_selene(configure_browser_options):
    browser.open('/ncr')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in Python'))


def test_search_no_result(configure_browser_options):
    browser.open('/ncr')
    browser.element('[name="q"]').should(be.blank).type('fhgfghjghFYUKRYUyru#$%#$%^&^&4*()&_56784563456').press_enter()
    browser.element('[id="botstuff"]').should(have.text('Your search - fhgfghjghFYUKRYUyru#$%#$%^&^&4*()&_56784563456 - did not match any documents.'))


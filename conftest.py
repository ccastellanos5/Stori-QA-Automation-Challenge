import pytest
from config.ios_capabilities import ios_capabilities
from config.android_capabilities import android_capabilities
from appium import webdriver


def get_capabilities(env):
    if env == 'android':
        return android_capabilities()
    elif env == 'ios':
        return ios_capabilities()
    else:
        raise ValueError(f"Environment '{env}' is not supported.")


def pytest_addoption(parser):
    parser.addoption('--env', default='android')


@pytest.fixture(scope="session")
def driver(request):
    env = request.config.getoption("env")
    capabilities = get_capabilities(env)

    driver = webdriver.Remote('http://localhost:4723', options=capabilities)
    driver.get('https://rahulshettyacademy.com/AutomationPractice/')
    yield driver

    # Teardown
    driver.quit()



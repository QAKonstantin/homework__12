import pytest
import os
import datetime
import random
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pathlib import Path


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--url", action="store", default="localhost")
    parser.addoption("--opencart_url", action="store", default="https://demo.opencart.com")
    parser.addoption("--drivers", action="store", default=os.path.expanduser("C:/driver"))
    parser.addoption("--log_level", action="store", default="DEBUG")
    parser.addoption("--bversion", action="store", default="99.0")
    parser.addoption("--vnc", action="store_true", default=False)
    parser.addoption("--logs", action="store_true", default=False)
    parser.addoption("--videos", action="store_true", default=False)


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    executor = request.config.getoption("--url")
    opencart_url = request.config.getoption("--opencart_url")
    drivers = request.config.getoption("--drivers")
    log_level = request.config.getoption("--log_level")
    version = request.config.getoption("--bversion")
    vnc = request.config.getoption("--vnc")
    logs = request.config.getoption("--logs")
    videos = request.config.getoption("--videos")

    if executor == "selenoid" or executor == "localhost":
        executor_url = f"http://{executor}:4444/wd/hub"

        caps = {
            "browserName": browser,
            "browserVersion": version,
            "screenResolution": "1280x1024",
            "name": "Opencart tests",
            "selenoid:options": {
                "sessionTimeout": "60s",
                "enableVNC": vnc,
                "enableVideo": videos,
                "enableLog": logs
            }
        }

        wd = webdriver.Remote(
            command_executor=executor_url,
            desired_capabilities=caps
        )


    else:
        if browser == "chrome":
            wd = webdriver.Chrome(service=Service(drivers + "/chromedriver.exe"))
        elif browser == "firefox":
            wd = webdriver.Firefox(service=Service(drivers + "/geckodriver.exe"))
        elif browser == "opera":
            wd = webdriver.Opera(service_args=Service(drivers + "/operadriver.exe"))

    wd.url = opencart_url
    wd.maximize_window()
    wd.get(wd.url)
    logger = logging.getLogger('driver')

    test_name = request.node.name

    logger.addHandler(logging.FileHandler(f"{Path(__file__).resolve().parent}/logs/{test_name}.log", mode='w'))
    logger.setLevel(level=log_level)
    logger.info("===> Test {} started at {}".format(test_name, datetime.datetime.now()))
    wd.test_name = test_name
    wd.log_level = log_level
    logger.info("Browser:{}".format(browser, wd.capabilities))

    def fin():
        with open(f"{Path(__file__).resolve().parent}/allure-results/environment.properties", 'w') as f:
            f.write(f'Browser={browser}\n')
            f.write(f'Browser.Version={version}\n')
            f.write(f'Executor={executor}')
        wd.quit()
        logger.info("===> Test {} finished at {}".format(test_name, datetime.datetime.now()))

    request.addfinalizer(fin)
    return wd


@pytest.fixture
def create_user():
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
               "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ]
    email = ''
    phone = '+7'
    for i in range(10):
        email += random.sample(letters, 1)[0]
        phone += random.sample(numbers, 1)[0]
    email += '@gmail.com'
    return (email, phone)

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as CS
from selenium.webdriver.firefox.service import Service as FS
from selenium.webdriver.edge.service import Service as ES
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

@pytest.fixture(autouse=True)
def setup(request, browser):
    if browser == "Chrome":
        driver = webdriver.Chrome(service=CS(ChromeDriverManager().install()))
    elif browser == "Firefox":
        driver = webdriver.Firefox(service=FS(GeckoDriverManager().install()))
    elif browser == "Edge":
         driver = webdriver.Edge(service=ES(EdgeChromiumDriverManager().install()))
    else:
         print("Provide valid browser")
    driver.get("https://www.yatra.com/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope="session", autouse=True)
def browser(request):
    return request.config.getoption("--browser")

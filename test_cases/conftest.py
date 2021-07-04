import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains


@pytest.fixture(scope="class")
def invokeBrowser(request):
    driver = webdriver.Chrome(executable_path="E:\\Code\PythonTestingSelenium\chromedriver.exe")
    driver.get("http://demowebshop.tricentis.com/")
    driver.maximize_window()

    request.cls.driver = driver
    yield
    driver.close()


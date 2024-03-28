import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function", autouse=False)
def driver():
    web_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    web_driver.implicitly_wait(5)
    web_driver.maximize_window()

    yield web_driver

    web_driver.quit()

@pytest.fixture(scope="function", autouse=False)
def accept_cookie(driver):
    try:
        cookie_overlay = driver.find_element(By.XPATH, '//*[@role="alertdialog"]')
        if cookie_overlay:
            accept_button = cookie_overlay.find_element(By.XPATH,
                            '//button[@id="onetrust-accept-btn-handler"]')
            accept_button.click()
    except Exception as e:
        print(f"Error handling cookies: {e}")

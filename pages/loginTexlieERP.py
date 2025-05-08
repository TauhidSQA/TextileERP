from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "http://172.16.2.61:8061/"

    def load(self):
        self.driver.get(self.url)
        self.driver.maximize_window()

    def login(self, username, password):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter your username']"))).send_keys(username)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Enter your password']").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]").click()

        wait.until(lambda d: "dashboard" in d.current_url.lower())

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import data
import locators


class Lk:

    @staticmethod
    def test_lk(driver):
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.CLASS_NAME, locators.entrance_button)))
        driver.find_element(By.CLASS_NAME, locators.entrance_button).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.CLASS_NAME, locators.entrance)))
        driver.find_element(By.XPATH, locators.email_login).send_keys(data.email_login)
        driver.find_element(By.XPATH, locators.password_registration).send_keys(data.password_send)
        driver.find_element(By.CLASS_NAME, locators.entrance_button).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.CLASS_NAME, locators.text_main)))
        driver.find_element(By.XPATH, locators.button_lk).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.CLASS_NAME, locators.exit_button)))
        assert driver.find_element(By.CLASS_NAME, locators.exit_button).text == "Выход"

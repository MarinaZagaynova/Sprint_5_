from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import data
import locators


class TestRegistration:

    def test_error_password(self, driver):
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, locators.button_lk)))
        driver.find_element(By.XPATH, locators.button_lk).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.CLASS_NAME, locators.entrance)))
        driver.find_element(By.LINK_TEXT, locators.registration).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.CLASS_NAME, locators.entrance)))
        driver.find_element(By.XPATH, locators.name_registration).send_keys(data.name_send)
        driver.find_element(By.XPATH, locators.email_registration).send_keys(data.email_send)
        driver.find_element(By.XPATH, locators.password_registration).send_keys(data.error_password)
        driver.find_element(By.CLASS_NAME, locators.register).click()
        assert driver.find_element(By.CLASS_NAME, locators.error_password).text == "Некорректный пароль"

    def test_correct_registration(self, driver):
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, locators.button_lk)))
        driver.find_element(By.XPATH, locators.button_lk).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.CLASS_NAME, locators.entrance)))
        driver.find_element(By.LINK_TEXT, locators.registration).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.CLASS_NAME, locators.entrance)))
        driver.find_element(By.XPATH, locators.name_registration).send_keys(data.name_send)
        driver.find_element(By.XPATH, locators.email_registration).send_keys(data.email_send)
        driver.find_element(By.XPATH, locators.password_registration).send_keys(data.password_reg)
        driver.find_element(By.CLASS_NAME, locators.register).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.LINK_TEXT, locators.registration)))
        assert driver.find_element(By.CLASS_NAME, locators.entrance_button).text == "Войти"

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import data
import locators
from tests.conftest import driver


class TestEntrance:

    def test_entrance_lk(self, driver):
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, locators.button_lk)))
        driver.find_element(By.XPATH, locators.button_lk).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.CLASS_NAME, locators.entrance)))
        driver.find_element(By.XPATH, locators.email_login).send_keys(data.email_login)
        driver.find_element(By.XPATH, locators.password_registration).send_keys(data.password_send)
        driver.find_element(By.CLASS_NAME, locators.entrance_button).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.CLASS_NAME, locators.text_main)))
        assert driver.find_element(By.CLASS_NAME, locators.entrance_button).text == "Оформить заказ"

    def test_entrance_main(self, driver):
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
        assert driver.find_element(By.CLASS_NAME, locators.entrance_button).text == "Оформить заказ"

    def test_entrance_registration(self, driver):
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, locators.button_lk)))
        driver.find_element(By.XPATH, locators.button_lk).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.CLASS_NAME, locators.entrance)))
        driver.find_element(By.LINK_TEXT, locators.registration).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.CLASS_NAME, locators.entrance)))
        driver.find_element(By.CLASS_NAME, locators.entrance_link).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.CLASS_NAME, locators.entrance)))
        driver.find_element(By.XPATH, locators.email_login).send_keys(data.email_login)
        driver.find_element(By.XPATH, locators.password_registration).send_keys(data.password_send)
        driver.find_element(By.CLASS_NAME, locators.entrance_button).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.CLASS_NAME, locators.text_main)))
        assert driver.find_element(By.CLASS_NAME, locators.entrance_button).text == "Оформить заказ"

    def test_entrance_password(self, driver):
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, locators.button_lk)))
        driver.find_element(By.XPATH, locators.button_lk).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.CLASS_NAME, locators.entrance)))
        driver.find_element(By.LINK_TEXT, locators.restore_password).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.CLASS_NAME, locators.entrance)))
        driver.find_element(By.CLASS_NAME, locators.entrance_link).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.CLASS_NAME, locators.entrance)))
        driver.find_element(By.XPATH, locators.email_login).send_keys(data.email_login)
        driver.find_element(By.XPATH, locators.password_registration).send_keys(data.password_send)
        driver.find_element(By.CLASS_NAME, locators.entrance_button).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.CLASS_NAME, locators.text_main)))
        assert driver.find_element(By.CLASS_NAME, locators.entrance_button).text == "Оформить заказ"

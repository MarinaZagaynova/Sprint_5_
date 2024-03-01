from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import data
import locators


class TestConstructor:
    def test_from_lk_to_constructor(self, driver):
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
        driver.find_element(By.LINK_TEXT, locators.constructor).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.CLASS_NAME, locators.text_main)))
        assert driver.find_element(By.CLASS_NAME, locators.text_main).text == "Соберите бургер"

    def test_constructor_souses(self, driver):
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
        driver.find_element(By.LINK_TEXT, locators.constructor).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.CLASS_NAME, locators.text_main)))
        driver.find_element(By.XPATH, locators.souses).click()
        assert "tab_tab_type_current__2BEPc" in driver.find_element(By.XPATH, locators.souses).get_attribute("class")

    def test_constructor_fillings(self, driver):
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
        driver.find_element(By.LINK_TEXT, locators.constructor).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.CLASS_NAME, locators.text_main)))
        driver.find_element(By.XPATH, locators.fillings).click()
        assert "tab_tab_type_current__2BEPc" in driver.find_element(By.XPATH, locators.fillings).get_attribute(
            "class")

    def test_constructor_buns(self, driver):
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
        driver.find_element(By.LINK_TEXT, locators.constructor).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.CLASS_NAME, locators.text_main)))
        driver.find_element(By.XPATH, locators.fillings).click()
        driver.find_element(By.XPATH, locators.buns).click()
        assert "tab_tab_type_current__2BEPc" in driver.find_element(By.XPATH, locators.buns).get_attribute(
            "class")

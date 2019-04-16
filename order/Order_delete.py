from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class OrderDelete(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://127.0.0.1:8080"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_order_delete(self):
        driver = self.driver
        driver.get(self.base_url + "/Showcase/orders.xhtml")
        driver.find_element_by_link_text("Create a new order").click()
        driver.find_element_by_id("clientName").clear()
        driver.find_element_by_id("clientName").send_keys("test")
        driver.find_element_by_id("amount").clear()
        driver.find_element_by_id("amount").send_keys("1")
        driver.find_element_by_id("orders_0").click()
        driver.find_element_by_link_text("refresh page").click()
        driver.find_element_by_xpath("(//a[contains(text(),'Delete')])[36]").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
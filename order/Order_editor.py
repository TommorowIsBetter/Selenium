# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class OrderEditor(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://192.168.1.166"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_order_editor(self):
        driver = self.driver
        driver.get(self.base_url + "/Showcase/orders?x")
        driver.find_element_by_link_text("Create a new order").click()
        driver.find_element_by_id("clientName").clear()
        driver.find_element_by_id("clientName").send_keys("teat_order")
        driver.find_element_by_id("amount").clear()
        driver.find_element_by_id("amount").send_keys("1")
        driver.find_element_by_id("orders_0").click()
        driver.find_element_by_xpath("(//a[contains(text(),'Edit')])[41]").click()
        driver.find_element_by_id("amount").clear()
        driver.find_element_by_id("amount").send_keys("2")

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

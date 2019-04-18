# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class Del(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://192.168.1.166"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_del(self):
        driver = self.driver
        driver.get(self.base_url + "/BookManager/")
        driver.find_element_by_link_text(u"图书列表").click()
        driver.find_element_by_link_text(u"添加图书").click()
        driver.find_element_by_name("product_name").clear()
        driver.find_element_by_name("product_name").send_keys("44")
        driver.find_element_by_name("product_price").clear()
        driver.find_element_by_name("product_price").send_keys("44")
        driver.find_element_by_name("product_nums").clear()
        driver.find_element_by_name("product_nums").send_keys("33")
        driver.find_element_by_name("product_desc").clear()
        driver.find_element_by_name("product_desc").send_keys("33")
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()
        driver.find_element_by_xpath(u"(//a[contains(text(),'删除')])[201]").click()

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

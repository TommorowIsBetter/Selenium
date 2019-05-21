#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2019/4/15 22:30
@description:在python路径下面放入geckodriver.exe，具体版本是64位即可。然后这里是火狐23和selenium2.35.0匹配。
"""

from selenium import webdriver
from time import sleep
driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
driver.maximize_window()
sleep(2)
driver.get("http://www.51zxw.net/list.aspx?page=3&cid=615")
driver.set_window_size(400,400)
driver.refresh()
sleep(2)
driver.back()
sleep(2)
driver.forward()
sleep(2)
driver.quit()

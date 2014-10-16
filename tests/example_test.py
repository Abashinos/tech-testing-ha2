#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import unittest
import urlparse

from selenium.webdriver import DesiredCapabilities, Remote, ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class Credentials():
    TTHA2LOGIN = 'tech-testing-ha2-1'
    TTHA2PASSWORD = 'Pa$$w0rD-1'
    DOMAIN = '@bk.ru'


class Page(object):
    BASE_URL = "https://target.mail.ru"
    PATH = ""

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = urlparse.urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)


class AuthPage(Page):
    PATH = "/login"

    @property
    def form(self):
        return AuthForm(self.driver)


class Component(object):
    def __init__(self, driver):
        self.driver = driver

    pass


class CreatePage(Page):
    PATH = "/ads/create"

    @property
    def top_menu(self):
        return TopMenu(self.driver)

    pass


class TopMenu(Component):
    EMAIL = "#PH_user-email"

    def get_email(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector('#PH_user-email').text
        )


class AuthForm(Component):
    ID_LOGIN = "id_Login"
    ID_DOMAIN = "id_Domain"
    ID_PASSWORD = "id_Password"
    ID_SUBMIT = "#gogogo>input"

    def set_login(self, login):
        self.driver.find_element_by_id(self.ID_LOGIN).send_keys(login)

    def set_password(self, password):
        self.driver.find_element_by_id(self.ID_PASSWORD).send_keys(password)

    def set_domain(self, domain):
        select = self.driver.find_element_by_id(self.ID_DOMAIN)
        Select(select).select_by_visible_text(domain)

    def submit(self):
        self.driver.find_element_by_css_selector(self.ID_SUBMIT).click()


class ExampleTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME.copy()
        )
        self.addCleanup(self.driver.quit)

    def test_wat(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()
        auth_form = auth_page.form

        auth_form.set_login(Credentials.TTHA2LOGIN)
        auth_form.set_password(Credentials.TTHA2PASSWORD)
        auth_form.set_domain(Credentials.DOMAIN)
        auth_form.submit()

        create_page = CreatePage(self.driver)
        create_page.open()
        email = TopMenu.get_email(create_page.top_menu)
        self.assertEqual(Credentials.TTHA2LOGIN + Credentials.DOMAIN, email)

        interests_wrapper = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_class_name('campaign-setting__wrapper_interests')
        )
        interests = interests_wrapper.find_element_by_class_name("campaign-setting__value")
        actions = ActionChains(self.driver)
        actions.move_to_element(interests_wrapper)
        actions.perform()
        actions.click(interests)
        actions.perform()

        #comp_interests = interests_wrapper.find_element_by_xpath(
        #   "//label[text()[contains(., 'Компьютерная техника и программы')]]")

        #comp_interests.find_element_by_class_name('tree__node__collapse-icon').click()

        banner_form = self.driver.find_element_by_class_name('banner-form')
        input = banner_form.find_element_by_xpath('.//input[@data-name="title"]')
        input.send_keys('see?')
        #banner_form.find_element_by_class_name('banner-form__input').click().send_keys('see?')


        import time
        time.sleep(10)


        # elem.send_keys('see?' + Keys.RETURN)


if __name__ == '__main__':
    unittest.main(verbosity=2)
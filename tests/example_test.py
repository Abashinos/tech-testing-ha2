#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import unittest
import urlparse

from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class Credentials(object):
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
        import time
        auth_page = AuthPage(self.driver)
        auth_page.open()
        auth_form = auth_page.form

        auth_form.set_login(Credentials.TTHA2LOGIN)
        auth_form.set_password(Credentials.TTHA2PASSWORD)
        auth_form.set_domain(Credentials.DOMAIN)
        auth_form.submit()

        create_page = CreatePage(self.driver)
        create_page.open()
        #email = TopMenu.get_email(create_page.top_menu)
        #self.assertEqual(Credentials.TTHA2LOGIN + Credentials.DOMAIN, email)
        """ Название кампании """
        name_box = WebDriverWait(self.driver, 30, 1).until(
            lambda d: d.find_element_by_class_name(
                'base-setting__campaign-name')
        )
        name_field = name_box.find_element_by_css_selector('[type="text"]')
        name_field.send_keys(Keys.CONTROL, "a")
        name_field.send_keys("Campaign")

        """ Площадка размещения """
        base_setting_box = WebDriverWait(self.driver, 30, 1).until(
            lambda d: d.find_element_by_class_name(
                'base-setting__row__body')
        )
        base_setting_box.find_element_by_xpath('.//input[@data-name="external_feed_abstract"]').click()

        """ Интересы """
        interests = WebDriverWait(self.driver, 30, 1).until(
            lambda d: d.find_element_by_class_name(
                'campaign-setting__wrapper_interests')
        )
        interests.find_element_by_css_selector("[data-node-id='interests'").click()

        comp_interests = WebDriverWait(interests, 30, 1).until(
            lambda d: d.find_element_by_xpath(
                '//span[@data-node-id="Компьютернаятехникаипрограммы"]'
            )
        )
        comp_interests.click()
        comp_interests = comp_interests.parent.find_element_by_class_name('tree__wrapper')

        for element in comp_interests.find_elements_by_class_name("tree__node__input"):
            element.click()

        chosen_box = interests.find_element_by_class_name('campaign-setting__chosen-box')
        chosen_value = WebDriverWait(chosen_box, 30, 1).until(
            lambda d: d.find_element_by_xpath(
                './/span[text() = "Компьютерная техника и программы"]'
            )
        ).parent

        WebDriverWait(interests, 30, 1).until(
            lambda d: d.find_element_by_class_name(
                'campaign-setting__chosen-box__item__close')
        ).click()

        """ Уровень дохода """
        income_group = WebDriverWait(self.driver, 30, 1).until(
            lambda d: d.find_element_by_css_selector('[data-name="income_group"]')
        )
        WebDriverWait(income_group, 30, 1).until(
            lambda d: d.find_element_by_class_name('campaign-setting__value')
        ).click()

        for element in income_group.find_elements_by_class_name('campaign-setting__input'):
            element.click()

        """ Создание объявления """
        banner_form = self.driver.find_element_by_class_name('banner-form')
        title = banner_form.find_element_by_xpath('.//input[@data-name="title"]')
        title.send_keys('see?')
        text = banner_form.find_element_by_xpath('.//textarea[@data-name="text"]')
        text.send_keys('see?')
        url = banner_form.find_element_by_xpath('.//li[@data-top="false"]//input[@data-name="url"]')
        url.send_keys('see.see')
        image = banner_form.find_element_by_xpath('.//input[@data-name="image"]')
        image.send_keys('/home/snake/Pictures/11.jpg')

        def waiting(d):
            banners = d.find_elements_by_class_name("banner-preview__img")
            for banner in banners:
                if banner.value_of_css_property("display") == 'block':
                    return banner

        banner = WebDriverWait(banner_form, 30, 1).until(waiting)

        WebDriverWait(banner, 30, 1).until(
            lambda d: (d.value_of_css_property("background-image") is not None)
        )

        submit = banner_form.find_element_by_class_name('banner-form__save-button')
        submit.click()

        """ Размещение объявления """
        self.driver.find_element_by_class_name("main-button-new").click()
        title = WebDriverWait(self.driver, 30, 1).until(
            lambda d: d.find_element_by_class_name("campaign-title")
        )

        """ Проверка результата """
        campaign_name = title.find_element_by_class_name("campaign-title__name").text
        self.assertEqual(campaign_name, 'Campaign')

        self.driver.find_element_by_class_name("control__link_edit").click()
        banner = WebDriverWait(self.driver, 30, 1).until(
            lambda d: d.find_element_by_class_name("added-banner")
        )
        self.assertEqual(banner.find_element_by_class_name("banner-preview__title").text, 'see?')



if __name__ == '__main__':
    unittest.main(verbosity=2)
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from page_objects.constants import *
from page_objects.pages import AuthPage, CreatePage
from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from tests.page_objects.components import TopMenu


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

        email = TopMenu.get_email(create_page.top_menu)
        self.assertEqual(Credentials.TTHA2LOGIN + Credentials.DOMAIN, email)

        """ Название кампании """
        name_box = create_page.campaign_name_box
        name_box.set_name(CampaignInfo.CAMPAIGN_NAME)

        """ Площадка размещения """
        pad_box = create_page.pad_radio_box
        pad_box.set_choice()

        """ Интересы """
        interests = create_page.interests_box
        interests.click_interests_dropdown()

        interests.click_comp_interests()
        interests.click_all_comp_interests()

        interests.close_chosen_box()

        """ Уровень дохода """
        income_group = create_page.income_group_box

        income_group.click_income_dropdown()

        income_group.click_all_income_groups()

        """ Создание объявления """
        banner_form = create_page.banner_form
        banner_form.fill_form()
        banner_form.submit()

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
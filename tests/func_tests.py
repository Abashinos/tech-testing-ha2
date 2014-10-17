#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support.wait import WebDriverWait

from components.constants import *
from page_objects.pages import AuthPage, CreatePage, CampaignsPage, EditPage


class FuncTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME.copy()
        )
        auth_page = AuthPage(self.driver)
        auth_page.open()
        auth_form = auth_page.form

        auth_form.set_login(Credentials.TTHA2LOGIN)
        auth_form.set_password(Credentials.TTHA2PASSWORD)
        auth_form.set_domain(Credentials.DOMAIN)
        auth_form.submit()

        self.create_page = CreatePage(self.driver)
        self.create_page.open()
        self.campaigns_page = CampaignsPage(self.driver)
        self.edit_page = EditPage(self.driver)
        self.addCleanup(self.driver.quit)

    def set_campaign_name(self):
        name_box = self.create_page.campaign_name_box
        name_box.set_name(CampaignInfo.CAMPAIGN_NAME)

    def set_ad_and_pad(self):
        ad_box = self.create_page.ad_radio_box
        ad_box.set_choice()
        pad_box = self.create_page.pad_radio_box
        pad_box.set_choice()

    def submit_banner(self):
        banner_form = self.create_page.banner_form
        banner_form.fill_form()
        banner_form.submit()

    def submit_campaign(self):
        self.driver.find_element_by_class_name(ElementsClasses.SUBMIT_CAMPAIGN).click()

    def set_up_test(self):
        self.set_campaign_name()
        self.set_ad_and_pad()
        self.submit_banner()

    def test_auth(self):
        email = self.create_page.top_menu.get_email()
        self.assertEqual(Credentials.TTHA2LOGIN + Credentials.DOMAIN, email)

    def test_create_campaign_submit_page(self):
        self.set_up_test()
        self.submit_campaign()
        campaign = self.campaigns_page.campaigns_component
        self.assertEqual(campaign.campaign_name, CampaignInfo.CAMPAIGN_NAME)
        self.assertEqual(campaign.banner_name, CampaignInfo.BANNER_TITLE)
        self.delete_campaign()

    def test_create_campaign_edit_page(self):
        self.set_up_test()
        self.submit_campaign()
        self.campaigns_page.campaigns_component.open_edit_page()
        banner_preview = self.edit_page.banner_preview
        self.assertEqual(banner_preview.banner_text, CampaignInfo.BANNER_TEXT)
        self.assertIsNotNone(banner_preview.check_image())
        self.delete_campaign()

    def test_create_campaign_with_interests(self):
        self.set_up_test()
        interests = self.create_page.interests_box
        interests.click_interests_dropdown()

        interests.click_comp_interests()
        interests.click_all_comp_interests()

        def assert_equal_interests(ins):
            return ins.get_chosen_box_text() == CampaignInfo.INTERESTS

        WebDriverWait(interests, Settings.WEBDRIVER_TIMEOUT, Settings.WEBDRIVER_POLL_FREQUENCY)\
            .until(assert_equal_interests)

        self.submit_campaign()
        campaign = self.campaigns_page.campaigns_component
        campaign.open_edit_page()
        interests_check = self.edit_page.interest_box
        self.assertEquals(interests_check.check_comp_interests(), "true")
        self.delete_campaign()

    def test_create_campaign_with_income_group(self):
        self.set_up_test()
        income_group = self.create_page.income_group_box
        income_group.click_income_dropdown()
        income_group.click_all_income_groups()

        def assert_equal_text(*args):
            return income_group.get_setting_text() == Settings.CHOSEN

        WebDriverWait(income_group, Settings.WEBDRIVER_TIMEOUT, Settings.WEBDRIVER_POLL_FREQUENCY)\
            .until(assert_equal_text)

        self.submit_campaign()
        campaign = self.campaigns_page.campaigns_component
        campaign.open_edit_page()
        income_group = self.edit_page.income_group_box
        income_group.click_income_dropdown()
        for element in income_group.driver.find_elements_by_class_name(ElementsClasses.INCOME_GROUPS):
            if element.get_attribute("checked") != "true":
                self.fail("Not all elements are checked")
        self.delete_campaign()

    def delete_campaign(self):
        self.campaigns_page.open()
        self.campaigns_page.campaigns_component.delete_campaign()



if __name__ == '__main__':
    unittest.main(verbosity=2)
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests.components.components import Component, ClassComponent

from tests.components.constants import ElementsCSS, ElementsXPath, ElementsClasses, CampaignInfo, Settings
from tests.page_objects.helpers import webdriver_search_by_css, webdriver_search_by_class, webdriver_search_by_xpath, \
    webdriver_search_by_id


class TopMenu(Component):
    ELEMENT_ID = "PH_user-email"

    def get_email(self):
        return webdriver_search_by_id(self.driver, self.ELEMENT_ID).text


class CampaignNameBox(ClassComponent):
    ELEMENT_CLASS = "base-setting__campaign-name"
    name_field = None

    def __init__(self, driver):
        super(CampaignNameBox, self).__init__(driver)
        self.name_field = webdriver_search_by_css(self.driver, ElementsCSS.CAMPAIGN_NAME_FIELD)

    def get_name_field(self):
        return self.name_field

    def set_name(self, name):
        self.name_field.clear()
        self.name_field.send_keys(name)


class AdRadioBox(ClassComponent):
    ELEMENT_CLASS = "base-setting__product-type"
    ad_choice = None

    def __init__(self, driver):
        super(AdRadioBox, self).__init__(driver)
        self.ad_choice = webdriver_search_by_xpath(self.driver, ElementsXPath.AD_LABEL)\
            .find_element_by_xpath("../input")

    def set_choice(self):
        self.ad_choice.click()


class PadRadioBox(ClassComponent):
    ELEMENT_CLASS = "base-setting__pads-targeting"
    pad_choice = None

    def __init__(self, driver):
        super(PadRadioBox, self).__init__(driver)
        self.pad_choice = webdriver_search_by_xpath(self.driver, ElementsXPath.PAD_LABEL)\
            .find_element_by_xpath("../input")

    def set_choice(self):
        self.pad_choice.click()


class InterestsBox(ClassComponent):
    ELEMENT_CLASS = "campaign-setting__wrapper_interests"
    comp_interests = None
    chosen_box = None

    def __init__(self, driver):
        super(InterestsBox, self).__init__(driver)
        self.comp_interests = webdriver_search_by_xpath(self.driver, ElementsXPath.COMP_INTERESTS_DROPDOWN)

    def click_interests_dropdown(self):
        webdriver_search_by_css(self.driver, ElementsCSS.INTERESTS_DROPDOWN).click()

    def form_chosen_box(self):
        self.chosen_box = self.driver.find_element_by_class_name(ElementsClasses.CHOSEN_BOX)

    def click_comp_interests(self):
        self.comp_interests.click()

    def click_all_comp_interests(self):
        self.form_chosen_box()
        comp_interests = self.comp_interests
        self.comp_interests = \
            self.comp_interests.parent.find_element_by_class_name(ElementsClasses.INTERESTS_TREE)

        for element in self.comp_interests.find_elements_by_class_name(ElementsClasses.INTERESTS_INPUT):
            element.click()

        self.comp_interests = comp_interests

    @staticmethod
    def check_interests(driver):
        WebDriverWait(driver, Settings.WEBDRIVER_TIMEOUT, Settings.WEBDRIVER_POLL_FREQUENCY).until_not(
            expected_conditions.staleness_of(webdriver_search_by_class(driver, ElementsClasses.CHOSEN_BOX_TEXT))
        )
        if webdriver_search_by_class(driver, ElementsClasses.CHOSEN_BOX_TEXT).text == CampaignInfo.INTERESTS:
            return True

    def wait_for_chosen_box(self):
        WebDriverWait(self.driver, Settings.WEBDRIVER_TIMEOUT, Settings.WEBDRIVER_POLL_FREQUENCY)\
            .until(self.check_interests)

    def close_chosen_box(self):
        webdriver_search_by_xpath(self.driver, ElementsXPath.CHOSEN_BOX)\
            .parent.find_element_by_class_name("campaign-setting__chosen-box__item__close").click()


class IncomeGroupBox(Component):
    ELEMENT_CSS = "[data-name='income_group']"
    income_groups = None
    setting_text = None

    def __init__(self, driver):
        driver = webdriver_search_by_css(driver, self.ELEMENT_CSS)
        super(IncomeGroupBox, self).__init__(driver)
        self.income_groups = self.driver.find_elements_by_class_name(ElementsClasses.INCOME_GROUPS)
        self.setting_text = self.driver.find_element_by_class_name(ElementsClasses.CAMPAIGN_SETTING_VALUE)

    def click_income_dropdown(self):
        WebDriverWait(self.driver, Settings.WEBDRIVER_TIMEOUT, Settings.WEBDRIVER_POLL_FREQUENCY).until(
            expected_conditions.element_to_be_clickable((By.CLASS_NAME, ElementsClasses.INCOME_DROPDOWN))
        ).click()

    def assert_equal_text(self, *args):
        if self.setting_text.text == Settings.CHOSEN:
            return True

    def check_income_text(self):
        WebDriverWait(self.driver, Settings.WEBDRIVER_TIMEOUT, Settings.WEBDRIVER_POLL_FREQUENCY)\
            .until(self.assert_equal_text)

    def click_all_income_groups(self):
        for income_group in self.income_groups:
            income_group.click()


class BannerForm(ClassComponent):
    ELEMENT_CLASS = "banner-form"
    banner = None
    title = None
    text = None
    url = None
    image = None
    submit_button = None

    def __init__(self, driver):
        super(BannerForm, self).__init__(driver)
        self.title = self.driver.find_element_by_xpath(ElementsXPath.BANNER_FORM_TITLE)
        self.text = self.driver.find_element_by_xpath(ElementsXPath.BANNER_FORM_TEXT)
        self.url = self.driver.find_element_by_xpath(ElementsXPath.BANNER_FORM_URL)
        self.image = self.driver.find_element_by_xpath(ElementsXPath.BANNER_FORM_IMAGE)
        self.submit_button = self.driver.find_element_by_class_name(ElementsClasses.BANNER_SUBMIT)

    @staticmethod
    def waiting(driver):
        banners = driver.find_elements_by_class_name("banner-preview__img")
        for banner in banners:
            if banner.value_of_css_property("display") == 'block':
                return banner

    def fill_form(self):
        self.title.send_keys(CampaignInfo.BANNER_TITLE)
        self.text.send_keys(CampaignInfo.BANNER_TEXT)
        self.url.send_keys(CampaignInfo.BANNER_URL)
        self.image.send_keys(CampaignInfo.BANNER_IMAGE)

        self.banner = WebDriverWait(self.driver, 30, 1).until(self.waiting)
        WebDriverWait(self.banner, 30, 1).until(
            lambda d: (d.value_of_css_property("background-image") is not None)
        )

    def submit(self):
        self.submit_button.click()


class SubmitButton(ClassComponent):
    ELEMENT_CLASS = "main-button-new"

    def __init__(self, driver):
        super(SubmitButton, self).__init__(driver)

    def click(self):
        self.driver.click()
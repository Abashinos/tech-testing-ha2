from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from tests.page_objects.constants import ElementsCSS, ElementsXPath, ElementsClasses, CampaignInfo
from tests.page_objects.helpers import webdriver_search_by_css, webdriver_search_by_class, webdriver_search_by_xpath, \
    webdriver_search_by_id


class Component(object):

    def __init__(self, driver):
        self.driver = driver


class ClassComponent(Component):
    ELEMENT_CLASS = None

    def __init__(self, driver):
        driver = webdriver_search_by_class(driver, self.ELEMENT_CLASS)
        super(ClassComponent, self).__init__(driver)


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
        self.name_field.send_keys(Keys.CONTROL, "a")
        self.name_field.send_keys(name)


class PadRadioBox(ClassComponent):
    ELEMENT_CLASS = "base-setting__pads-targeting"
    pad_choice = None

    def __init__(self, driver):
        super(PadRadioBox, self).__init__(driver)
        self.pad_choice = webdriver_search_by_xpath(self.driver, ElementsXPath.PAD_CHOICE)

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

    def close_chosen_box(self):
        webdriver_search_by_xpath(self.driver, ElementsXPath.CHOSEN_BOX)\
            .parent.find_element_by_class_name("campaign-setting__chosen-box__item__close").click()


class IncomeGroupBox(Component):
    ELEMENT_CSS = "[data-name='income_group']"
    income_groups = None

    def __init__(self, driver):
        driver = webdriver_search_by_css(driver, self.ELEMENT_CSS)
        super(IncomeGroupBox, self).__init__(driver)
        self.income_groups = self.driver.find_elements_by_class_name(ElementsClasses.INCOME_GROUPS)

    def click_income_dropdown(self):
        webdriver_search_by_class(self.driver, ElementsClasses.INCOME_DROPDOWN).click()

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


class AuthForm(Component):
    ELEMENT_ID = "swa_auth"
    ID_LOGIN = "id_Login"
    ID_DOMAIN = "id_Domain"
    ID_PASSWORD = "id_Password"
    ID_SUBMIT = "#gogogo>input"

    def __init__(self, driver):
        driver = webdriver_search_by_id(driver, self.ELEMENT_ID)
        super(AuthForm, self).__init__(driver)

    def set_login(self, login):
        self.driver.find_element_by_id(self.ID_LOGIN).send_keys(login)

    def set_password(self, password):
        self.driver.find_element_by_id(self.ID_PASSWORD).send_keys(password)

    def set_domain(self, domain):
        select = self.driver.find_element_by_id(self.ID_DOMAIN)
        Select(select).select_by_visible_text(domain)

    def submit(self):
        self.driver.find_element_by_css_selector(self.ID_SUBMIT).click()
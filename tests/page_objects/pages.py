import urlparse
from tests.page_objects.components import *


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


class CreatePage(Page):
    PATH = "/ads/create"

    @property
    def top_menu(self):
        return TopMenu(self.driver)

    @property
    def campaign_name_box(self):
        return CampaignNameBox(self.driver)

    @property
    def pad_radio_box(self):
        return PadRadioBox(self.driver)

    @property
    def interests_box(self):
        return InterestsBox(self.driver)

    @property
    def income_group_box(self):
        return IncomeGroupBox(self.driver)

    @property
    def banner_form(self):
        return BannerForm(self.driver)

    pass



import urlparse
from tests.components.components_auth import *
from tests.components.components_campaigns import CampaignsComponent

from tests.components.components_create import *
from tests.components.components_edit import BannerPreview, InterestBox


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
    def ad_radio_box(self):
        return AdRadioBox(self.driver)

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


class CampaignsPage(Page):
    PATH = "/ads/campaigns"

    @property
    def campaigns_component(self):
        return CampaignsComponent(self.driver)


class EditPage(Page):
    @property
    def banner_preview(self):
        return BannerPreview(self.driver)

    @property
    def interest_box(self):
        return InterestBox(self.driver)

    @property
    def income_group_box(self):
        return IncomeGroupBox(self.driver)

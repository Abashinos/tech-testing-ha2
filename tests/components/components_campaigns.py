from tests.components.components import Component, ClassComponent
from tests.components.constants import ElementsClasses
from tests.page_objects.helpers import webdriver_search_by_class

__author__ = 'snake'


class CampaignsComponent(ClassComponent):
    ELEMENT_CLASS = "campaign-row"
    edit_button = None
    delete_button = None
    campaign_name = None
    banner_name = None

    def __init__(self, driver):
        super(CampaignsComponent, self).__init__(driver)
        self.campaign_name = webdriver_search_by_class(self.driver, ElementsClasses.CAMPAIGN_TITLE).text
        self.banner_name = webdriver_search_by_class(self.driver, ElementsClasses.BANNER_NAME).text
        self.edit_button = webdriver_search_by_class(self.driver, ElementsClasses.EDIT_BUTTON)
        self.delete_button = webdriver_search_by_class(self.driver, ElementsClasses.DELETE_BUTTON)

    def open_edit_page(self):
        self.edit_button.click()

    def delete_campaign(self):
        self.delete_button.click()

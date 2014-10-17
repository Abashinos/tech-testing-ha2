from selenium.webdriver.support.wait import WebDriverWait
from tests.components.components import ClassComponent
from tests.components.constants import ElementsClasses, ElementsXPath
from tests.page_objects.helpers import webdriver_search_by_class, webdriver_search_by_xpath

__author__ = 'snake'


class BannerPreview(ClassComponent):
    ELEMENT_CLASS = "added-banner"
    banner_text = None
    banner_img = None

    def __init__(self, driver):
        super(BannerPreview, self).__init__(driver)
        self.banner_text = webdriver_search_by_class(self.driver, ElementsClasses.BANNER_PREVIEW_TEXT).text
        self.banner_img = webdriver_search_by_class(self.driver, ElementsClasses.BANNER_PREVIEW_IMG)

    def check_image(self):
        return self.banner_img.value_of_css_property("background-image")


class InterestBox(ClassComponent):
    ELEMENT_CLASS = "campaign-setting__wrapper_interests"
    comp_interests = None

    def __init__(self, driver):
        super(InterestBox, self).__init__(driver)
        self.comp_interests = webdriver_search_by_xpath(self.driver, ElementsXPath.COMP_INTERESTS_CHECKBOX)

    def check_comp_interests(self):
        return self.comp_interests.get_attribute("checked")


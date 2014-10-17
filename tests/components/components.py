from tests.page_objects.helpers import webdriver_search_by_class


class Component(object):

    def __init__(self, driver):
        self.driver = driver


class ClassComponent(Component):
    ELEMENT_CLASS = None

    def __init__(self, driver):
        driver = webdriver_search_by_class(driver, self.ELEMENT_CLASS)
        super(ClassComponent, self).__init__(driver)
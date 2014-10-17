from selenium.webdriver.support.wait import WebDriverWait

from tests.components.constants import Settings


def webdriver_search_by_class(driver, class_name):
    return WebDriverWait(driver, Settings.WEBDRIVER_TIMEOUT, Settings.WEBDRIVER_POLL_FREQUENCY).until(
        lambda d: d.find_element_by_class_name(class_name)
    )


def webdriver_search_by_css(driver, css):
    return WebDriverWait(driver, Settings.WEBDRIVER_TIMEOUT, Settings.WEBDRIVER_POLL_FREQUENCY).until(
        lambda d: d.find_element_by_css_selector(css)
    )


def webdriver_search_by_xpath(driver, xpath):
    return WebDriverWait(driver, Settings.WEBDRIVER_TIMEOUT, Settings.WEBDRIVER_POLL_FREQUENCY).until(
        lambda d: d.find_element_by_xpath(xpath)
    )


def webdriver_search_by_id(driver, id):
    return WebDriverWait(driver, Settings.WEBDRIVER_TIMEOUT, Settings.WEBDRIVER_POLL_FREQUENCY).until(
        lambda d: d.find_element_by_id(id)
    )
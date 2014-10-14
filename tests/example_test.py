import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class ExampleTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.addCleanup(self.browser.quit)

    def test_wat(self):
        self.browser.get('http://www.google.com')
        elem = self.browser.find_element_by_id('gbqfq')

        elem.send_keys('see?' + Keys.RETURN)


if __name__ == '__main__':
    unittest.main(verbosity=2)
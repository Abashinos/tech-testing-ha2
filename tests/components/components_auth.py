from selenium.webdriver.support.select import Select
from tests.components.components import Component
from tests.page_objects.helpers import webdriver_search_by_id


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
from Pages.BasePage import BasePage
from Utils.tools import read_json_file
from Locators import login_page_locators as login_locators


class Login(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.customer = read_json_file('../Test_data/users.json')

    def insert_email(self):
        email = self.customer['email']
        self.send_keys(locator=login_locators.username_textbox, key=email)

    def insert_password(self):
        password = self.customer['password']
        self.send_keys(locator=login_locators.password_textbox, key=password)

    def click_login(self):
        self.click_on_element(locator=login_locators.login_button)

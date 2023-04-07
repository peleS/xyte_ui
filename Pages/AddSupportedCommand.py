from Pages.BasePage import BasePage
from Locators import add_supported_command_locators as supported_locators


class AddSupportedCommand(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def insert_command_name(self, text: str):
        self.send_keys(key=text, locator=supported_locators.name)

    def insert_description(self, text: str):
        self.send_keys(key=text, locator=supported_locators.description)

    def insert_name_on_device(self, text: str):
        self.send_keys(key=text, locator=supported_locators.name_on_device)

    def click_create_button(self):
        self.click_on_element(locator=supported_locators.create_button)

    def get_error_header(self):
        self.get_element_by_locator(locator=supported_locators.supported_command_error)


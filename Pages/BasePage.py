from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click_on_element(self, locator: tuple):
        try:
            WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(locator)).click()
        except TimeoutException:
            print(f'Element {locator} was not found - Time Exception reached')
            assert False

    def get_element_by_locator(self, locator: tuple):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
            return element
        except TimeoutException:
            print(f'Element {locator} was not found - Time Exception reached')
            assert False

    def get_element_text(self, locator: tuple) -> str:
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
            return element.text
        except TimeoutException:
            print(f'Element {locator} was not found - Time Exception reached')
            assert False

    def get_page_title(self, title: str):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title

    def get_expected_url(self, expected_url: str) -> str:
        url = WebDriverWait(self.driver, 10).until(EC.url_matches(expected_url))
        return str(url)

    def element_exists(self, locator: tuple) -> None:
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            print(f'Element {locator} was not found - Time Exception reached')
            assert False

    def send_keys(self, key, locator: tuple):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator)).send_keys(key)
        except TimeoutException:
            print(f'Element {locator} was not found - Time Exception reached')
            assert False

    def open_page(self, url: str):
        self.driver.get(url)

    def find_if_value_in_table(self, locator: tuple, name: str):
        """
        :param locator: the table locator we wish to check
        :param name: the value name we wish to look for
        :return: boolean , True if the name is found in the table False if not
        """
        # All the Name column cells have an id with 'cell-cell_#_name' where # is a number from 0 to end of the column
        # I could iterate over the actual table but since all i have to do is validate the new
        # item appears in the table i can just look at the raw text , its faster
        table = self.get_element_by_locator(locator)
        if name in table.text:
            return True
        return False



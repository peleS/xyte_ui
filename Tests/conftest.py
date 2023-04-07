import pytest

from Pages.AddSupportedCommand import AddSupportedCommand
from Pages.LoginPage import Login
from Pages.ModelDetails import ModelDetails
from Pages.SideBar import SideBar
from Pages.ModelsPage import Models
from selenium import webdriver

from Pages.SupportedCommands import SupportedCommands


@pytest.fixture(scope='function')
def set_driver():
    driver = webdriver.Chrome('../Drivers/chromedriver_112_0_5615_49.exe')
    yield driver
    # I can add a cleanup option here to delete the new model or i can use a hook instead
    driver.quit()


@pytest.fixture(scope='function')
def login_page_fixture(set_driver):
    login = Login(set_driver)
    yield login


@pytest.fixture(scope='function')
def side_bar_fixture(set_driver):
    sidebar = SideBar(set_driver)
    yield sidebar


@pytest.fixture(scope='function')
def models_fixture(set_driver):
    models = Models(set_driver)
    yield models


@pytest.fixture(scope='function')
def model_details_fixture(set_driver):
    details = ModelDetails(set_driver)
    yield details


@pytest.fixture(scope='function')
def add_supported_command_fixture(set_driver):
    command = AddSupportedCommand(set_driver)
    yield command


@pytest.fixture(scope='function')
def supported_command_fixture(set_driver):
    tab = SupportedCommands(set_driver)
    yield tab

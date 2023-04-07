import time
from Utils.tools import generate_new_command_values
from Locators import side_bar_locators as sidebar_locators
from Locators import models_locators, model_details_locators, supported_command_locators as supported_locators


class TestSupportCommands:

    def test_add_command_to_model(self,
                                  login_page_fixture,
                                  side_bar_fixture,
                                  models_fixture,
                                  model_details_fixture,
                                  add_supported_command_fixture,
                                  supported_command_fixture):
        values = generate_new_command_values()

        expected = 'https://partners.xyte.io/home'
        login_page_fixture.open_page(expected)
        login_page_fixture.insert_email()
        login_page_fixture.insert_password()
        login_page_fixture.click_login()
        login_page_fixture.get_expected_url(expected)

        side_bar_fixture.click_on_models(sidebar_locators.models)

        models_fixture.find_model(models_locators.model_name_747)
        models_fixture.click_on_element(models_locators.model_name_747)
        models_fixture.click_on_element(model_details_locators.supported_commands)

        command_exists = models_fixture.find_if_value_in_table(supported_locators.commands_table, name=values["name"])
        assert not command_exists, f'Error, Command is already in the commands table, cant start test: {values["name"]}'

        supported_command_fixture.click_on_element(supported_locators.add_command)

        add_supported_command_fixture.insert_command_name(text=values['name'])
        add_supported_command_fixture.insert_description(text=values['description'])
        add_supported_command_fixture.insert_name_on_device(text=values['name_on_device'])
        add_supported_command_fixture.click_create_button()

        time.sleep(5)

        command_exists = models_fixture.find_if_value_in_table(supported_locators.commands_table, name=values["name"])
        assert command_exists, f'Error, Command was not found in the commands table : {values["name"]}'

        print(f'Test Completed command {values["name"]} was added to the supported commands')

        # FIXME: Since there seems to be a limit to the amount of commands (Bug? / Design?)
        #  there should be a cleanup function at the end to remove all previous commands besides the default ones

    def test_duplicate_command_fails(self,
                                     login_page_fixture,
                                     side_bar_fixture,
                                     models_fixture,
                                     model_details_fixture,
                                     add_supported_command_fixture,
                                     supported_command_fixture):

        # can add this to test data
        expected = 'https://partners.xyte.io/home'
        login_page_fixture.open_page(expected)
        login_page_fixture.insert_email()
        login_page_fixture.insert_password()
        login_page_fixture.click_login()
        login_page_fixture.get_expected_url(expected)

        side_bar_fixture.click_on_models(sidebar_locators.models)

        models_fixture.find_model(models_locators.model_name_747)
        models_fixture.click_on_element(models_locators.model_name_747)
        models_fixture.click_on_element(model_details_locators.supported_commands)

        command_exists = models_fixture.find_if_value_in_table(supported_locators.commands_table, name='reboot')
        assert command_exists, f'Error, Command is not in the commands table, cant start test: reboot'

        supported_command_fixture.click_on_element(supported_locators.add_command)

        add_supported_command_fixture.insert_command_name(text='reboot')
        add_supported_command_fixture.insert_description(text='Reboot the device')
        add_supported_command_fixture.insert_name_on_device(text='reboot')
        add_supported_command_fixture.click_create_button()

        add_supported_command_fixture.get_error_header()

        # Should add a validation that there really isn't a duplicate of the command in the table


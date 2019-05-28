class Locators:
    '''
    These are the page locators
    '''

    # Login page objects
    username_textbox_name = "ccUsername"
    password_textbox_name = "ccPassword"
    login_button_xpath = "//button[@type='submit'][contains(.,'Log in')]"

    # Home page objects
    logout_button_xpath = "//button[contains(@data-original-title,'Log out')]"
    logout_confirm_xpath = '//*[@id="ccConfirmWindowY"]'
    dropdown_datapoints_xpath = "//a[@class='nav-link dropdown-toggle'][contains(.,'Data points')]"
    dropdown_item_datapoints_xpath = "//a[@class='dropdown-item'][contains(.,'Data points')]"

    # Station configuration objects
    dropdown_process_access_id = "navbarDropdown3"
    station_configuration_linktext = "Station configuration"
    station_name_textbox_xpath = '//*[@id="ccStationName"]'
    add_button_id = "ccStationAdd"
    confirm_window_xpath = "//button[@type='button'][contains(.,'OK')]"
    s7_tab_link_xpath = "//a[@class='nav-item nav-link cc-station-s7'][contains(.,'S7')]"
    ip_address_textbox_id = "ccStationS7Address"
    controller_family_id = "ccStationS7Controller"
    save_button_xpath = "//button[@type='submit'][contains(.,'Save')]"
    apply_button_id = "ccApply"

    # Firmware page objects
    dropdown_maintenance_id = "navbarDropdown7"
    maintenance_linktext = "Firmware"
    firmware_file_input_id = "ccFirmwareFile"
    update_firmware_button_id = "ccFirmwareImport"
    firmware_update_confirm_window = "//button[@type='button'][contains(.,'Yes')]"








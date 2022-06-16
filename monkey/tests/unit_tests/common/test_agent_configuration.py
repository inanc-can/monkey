from common.configuration import CustomPBAConfigurationSchema, PluginConfigurationSchema


def test_build_plugin_configuration():
    name = "bond"
    options = {"gun": "Walther PPK", "car": "Aston Martin DB5"}
    schema = PluginConfigurationSchema()

    config = schema.load({"name": name, "options": options})

    assert config.name == name
    assert config.options == options


def test_custom_pba_configuration_schema():
    linux_command = "a"
    linux_filename = "b"
    windows_command = "c"
    windows_filename = "d"
    schema = CustomPBAConfigurationSchema()

    config = schema.load(
        {
            "linux_command": linux_command,
            "linux_filename": linux_filename,
            "windows_command": windows_command,
            "windows_filename": windows_filename,
        }
    )

    assert config.linux_command == linux_command
    assert config.linux_filename == linux_filename
    assert config.windows_command == windows_command
    assert config.windows_filename == windows_filename

import toml
from pathlib import Path


#: Path of the configuration file from an unpacked Path list.
conf_file: Path
(conf_file,) = list(Path.cwd().parent.glob("**/conf.toml"))


class Settings:
    """
    Creates an object containing application configuration from a deserialized
    file.  The class will attempt to recursively walk any nested object, so:

    ::

      [section]
      variable = "value"

    becomes ``.section.variable`` which, when called returns ``"value"``. Each
    Key representing another nested layer will be of a type ``Settings()``.
    """

    def __init__(self, config) -> None:
        for k, v in config.items():
            if isinstance(v, dict):
                setattr(self, k, Settings(v))
            else:
                setattr(self, k, v)


#: Reads the config file.
with open(conf_file, "r") as fp:
    config = toml.load(fp)

#: An instance of the settings class for use in the application.
settings = Settings(config)

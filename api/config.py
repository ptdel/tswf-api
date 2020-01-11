import toml


class Settings:
    def __init__(self, config):
        """ Just walk the toml file. """
        for k, v in config.items():
            if isinstance(v, dict):
                setattr(self, k, Settings(v))
            else:
                setattr(self, k, v)


with open("conf.toml", "r") as fp:
    config = toml.load(fp)


settings = Settings(config)

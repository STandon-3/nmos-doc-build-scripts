import yaml

SRC_DIR = r"source-repo"
_CONFIG_YML = r"_config.yml"


def get_config():
    """Returns a dict created from YAML config for the spec"""
    with open(_CONFIG_YML) as file:
        return yaml.load(file, Loader=yaml.FullLoader)

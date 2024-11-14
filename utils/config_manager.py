import atexit
import sys, os
import json

from dataclasses import asdict, dataclass, fields
from utils import script_abs_path

DEFAULT_CONFIG_FILE_NAME = "config.json"

@dataclass
class ConfigFile:
    device_ip1: str = ""
    sync_clipboard: bool = True

class ConfigManager:
    path: str
    config: ConfigFile
    is_first_use: bool

    def __init__(self):
        file_path = self.path = ConfigManager.storage_path()
        is_exists = self.is_first_use = os.path.exists(file_path)
        if not is_exists: ConfigManager.create_default_config(file_path)
        self.config = ConfigManager.read_config(file_path)
        atexit.register(self.save)

    def save(self):
        config_dict = asdict(self.config)
        with open(self.path, "w") as f:
            json.dump(config_dict, f, indent=4)

    @staticmethod
    def create_default_config(path: str):
        default_config = ConfigFile()
        config_json = json.dumps(asdict(default_config))
        with open(path, "w") as f: f.write(config_json)

    @staticmethod
    def read_config(path: str) -> ConfigFile:
        with open(path, "r") as f: config_content = json.load(f)
        if type(config_content) != dict: return ConfigFile()

        expected_fields = {f.name: f.type for f in fields(ConfigFile)}
        filtered_fields = {}
        for key, item in config_content.items():
            if key not in expected_fields: continue
            if type(item) != expected_fields[key]: continue
            filtered_fields[key] = item
        return ConfigFile(**filtered_fields)

    @staticmethod
    def storage_path() -> str:
        if getattr(sys, "frozen", False):
            config_base_dir = os.path.dirname(sys.executable)
        else:
            script_path = script_abs_path(__file__)
            config_base_dir = script_path.parent
        config_path = os.path.join(config_base_dir, DEFAULT_CONFIG_FILE_NAME)
        return config_path

CONFIG = ConfigManager()
import threading
import json


class SingletonMeta(type):
    """
    To ensure only one instance of config loader is created
    and shared throughout the application
    """

    def __init__(cls, *args, **kwargs):
        super().__init__(*args, **kwargs)
        cls._instance = None
        cls._locker = threading.Lock()

    @property
    def instance(self, *args, **kwargs):
        if self._instance is None:
            with self._locker:
                if self._instance is None:
                    self._instance = self(*args, **kwargs)
        return self._instance


class Configuration(metaclass=SingletonMeta):
    def __init__(self):
        self.config = self.load()

    def load(self):
        with open("config/config.json") as f:
            config = json.load(f)
        return config

    def get(self, value):
        return self.config.get(f"{value}")

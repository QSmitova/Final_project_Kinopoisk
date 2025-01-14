import json
import os
from pathlib import Path


class DataProvider(dict):
    def __init__(self) -> None:
        super().__init__()
        file_path = Path(os.path.dirname(os.path.abspath(__file__))) / "test_data.json"
        with open(file_path, "r") as data_file:
            self.update(**json.load(data_file))

    def getint(self, prop: str) -> int:
        val = self.get(prop)
        return int(val)

    def get_api_token(self) -> str:
        return self.get("API_TOKEN")

    def get_email(self) -> str:
        return self.get("email")

    def get_password(self) -> str:
        return self.get("password")

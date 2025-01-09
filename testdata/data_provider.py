import json


class DataProvider(dict):

    def __init__(self)-> None:
        super().__init__()
        with open('test_data.json', "r") as my_file:
            self.update(**json.load(my_file))

    def getint(self, prop:str) -> int:
        val = self.get(prop)
        return int(val)

    def get_key(self) -> str:
        return self.get("KEY")

    def get_value(self) -> str:
        return self.get("VALUE")

    def get_email(self) -> str:
        return self.get("email")

    def get_password(self) -> str:
        return self.get("password")

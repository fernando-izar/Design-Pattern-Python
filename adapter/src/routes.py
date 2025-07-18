from src.controller import write_in_db
from src.helper.adapter import Adapter


def route1(message):
    Code().handle(message)


def route2(message):
    process = Adapter(Code())
    process.handle(message)


class Code:

    def handle(self, message):
        token = message["header"]["token"]
        if token:
            print("Authenticating token...")
            write_in_db(message["body"]["name"], message["body"]["message"])

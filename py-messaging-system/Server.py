from Wrapper import *
from Distributor import Distributor
from BaseRequest import BaseRequest

# Each request functionality is described in the server file


class GetServerTime(BaseRequest):
    def uri(self):
        return "/get-server-time"

    def get(self, headers):
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


class Multiply(BaseRequest):
    def uri(self):
        return "/multiply"

    def post(self, headers, body):
        numbers = str(body).split(",")
        x = int(numbers[0][2:])
        y = int(numbers[1][:-1])
        return str(x*y)


class GetReqCount(BaseRequest):
    def uri(self):
        return "/get-req-count"

    def get(self, headers):
        return str(Handlers.req_counter)

# The server class adds the request responses we've created to its distributor, and set the port for the wrapper to run
# the server on


class Server(object):

    def __init__(self):
        self.distributor = Distributor()

        self.distributor.add(GetServerTime())
        self.distributor.add(Multiply())
        self.distributor.add(GetReqCount())

        self.wrapper = Wrapper(distributor=self.distributor)
        self.wrapper.run(port=4657)


def run():
    Server()


if __name__ == "__main__":
    run()

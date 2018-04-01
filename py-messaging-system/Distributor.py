from BaseRequest import BaseRequest

# The Distributor class enables us to add request functionality - scalability and de-coupling


class Distributor(object):

    def __init__(self):
        self.requests = {}

    def add(self, request: BaseRequest):
        self.requests[request.uri()] = request

    def remove(self, uri):
        self.requests.pop(uri)

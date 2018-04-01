# Base request functionality


class BaseRequest(object):
    def uri(self):
        return "specific/path/uri"

    def get(self, headers):
        return "get_res"

    def post(self, headers, body):
        return "post_res"

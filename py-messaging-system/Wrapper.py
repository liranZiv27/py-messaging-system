from http.server import BaseHTTPRequestHandler, HTTPServer
import ssl

# Handlers provide the basic HTTP request handling


class Handlers(BaseHTTPRequestHandler):

    distributor = None
    req_counter = 0

    def _set_headers_success(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def _set_headers_not_found(self):
        self.send_response(404)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

# Each request increment the request counter
    def do_GET(self):
        Handlers.req_counter += 1
        uri = self.path
        headers = self.headers["testhd"]

# In order to get the correct URI and success code
        try:
            response = Handlers.distributor.requests[uri].get(headers)
            self._set_headers_success()
            self.wfile.write(response.encode("utf-8"))
        except Exception:
            self._set_headers_not_found()

    def do_POST(self):
        Handlers.req_counter += 1

        body = self.rfile.read(int(self.headers['Content-Length']))
        uri = self.path
        headers = self.headers

        try:
            response = Handlers.distributor.requests[uri].post(headers, body)

            self._set_headers_success()
            self.wfile.write(response.encode("utf-8"))
        except Exception:
            self._set_headers_not_found()

# The Wrapper class runs the server with the required param (addr, port)


class Wrapper(object):

    def __init__(self, distributor):
        self.distributor = distributor

    def run(self, port=80):
        server_address = ('', port)

        Handlers.distributor = self.distributor
        httpd = HTTPServer(server_address, Handlers)
        httpd.socket = ssl.wrap_socket(httpd.socket, certfile='server.pem', server_side=True)

        print(f'Server is Running, port: {port}')
        httpd.serve_forever()

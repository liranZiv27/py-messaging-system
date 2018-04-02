# py-messaging-system
HTTP web server replies with the required responses

1. I chose to use HTTPS protocol for this project

2. I'm using self-signed certificate of course

3. In the Handlers class, we need to use 'distributor' and 'req_counter' as instance var instead of static var, that way we can use as many instances as we like

4. The error handling support is minimal

5. Using BaseRequest to define requests is an overkill underI the current request set, but it can be useful if we have many requests

6. The Handlers class determines the behaviour of each request received

7. We can add as many request responses in the Server.py file

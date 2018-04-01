1. I chose to use HTTPS protocol for this project

2. i'm using self-signed certificate of course

1. In the Handlers class, we need to use 'distributor' and 'req_counter' as instance var instead of static var, that way we
can use as many instances as we like

2. The error handling support ia minimal

3. Using BaseRequest to define requests is an overkill under the current
request set, but it can be useful if we have many requests
import requests

class RequestUtil:

    def send_request(self, method, url, **kwargs):
        response = requests.request(method, url, **kwargs)
        return response
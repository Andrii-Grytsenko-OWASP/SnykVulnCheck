import requests

from src.helpers.enums import ErrorMessages
from src.helpers.utils import get_url


class ApiClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()

    def get(self, endpoint: str, *args, **kwargs):
        return self.session.get(url=get_url(self.base_url, endpoint),
                                *args, **kwargs)

    def post(self):
        raise NotImplemented(ErrorMessages.NOT_IMPLEMENTED_YET)

    def put(self):
        raise NotImplemented(ErrorMessages.NOT_IMPLEMENTED_YET)

    def patch(self):
        raise NotImplemented(ErrorMessages.NOT_IMPLEMENTED_YET)

    def delete(self):
        raise NotImplemented(ErrorMessages.NOT_IMPLEMENTED_YET)

    def options(self):
        raise NotImplemented(ErrorMessages.NOT_IMPLEMENTED_YET)

    def head(self):
        raise NotImplemented(ErrorMessages.NOT_IMPLEMENTED_YET)

    def trace(self):
        raise NotImplemented(ErrorMessages.NOT_IMPLEMENTED_YET)

    def connect(self):
        raise NotImplemented(ErrorMessages.NOT_IMPLEMENTED_YET)

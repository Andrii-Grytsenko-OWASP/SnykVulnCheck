from src.config import CFG
from src.http_client.api_client import ApiClient
from src.http_client.api_response import *
from src.helpers.enums import ApiResponseType


class SnykApi:
    def __init__(self):
        self.api = ApiClient(CFG.SNYK_API_URL)

    def get_vulnerabilities(self, component: str) -> ApiResponse:
        response = self.api.get(CFG.SNYK_API_ENDPOINT, params={CFG.SNYK_API_PARAM: component})
        return ApiResponse(
            response.status_code,
            ApiResponseType.ok if response.status_code < 300 else ApiResponseType.error,
            response.json() if response.status_code < 300 else response.text
        )


API = SnykApi()

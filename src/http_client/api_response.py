from src.helpers.enums import ApiResponseType


class ApiResponse:
    def __init__(self, code: int, response_type: ApiResponseType, data):
        self.code = code
        self.type = response_type
        self.data = data

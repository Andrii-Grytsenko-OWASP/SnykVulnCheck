from enum import Enum


class ApiResponseType(Enum):
    ok = "OK"
    warning = "Warning"
    info = "Info"
    error = "Error"


class ErrorMessages:
    NOT_IMPLEMENTED_YET = "Not implemented yet"

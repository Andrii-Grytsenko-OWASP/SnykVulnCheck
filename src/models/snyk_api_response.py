from alchemize import Attr, JsonMappedModel
from src.models.snyk_api_classes import SnykVulnerability


class SnykApiResponse(JsonMappedModel):
    __mapping__ = {
        "status": Attr("status", str),
        "vulnerabilities": Attr("vulnerabilities", [SnykVulnerability]),
    }

    def __init__(self, status: str = None, vulnerabilities: [SnykVulnerability] = None):
        self.status = status
        self.vulnerabilities = list(vulnerabilities) if vulnerabilities is not None else []

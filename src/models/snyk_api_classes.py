from alchemize import Attr, JsonMappedModel


class SnykSemver(JsonMappedModel):
    __mapping__ = {
        "vulnerable": Attr("vulnerable", [str]),
    }

    def __init__(self, vulnerable: [str] = None):
        self.vulnerable = list(vulnerable) if vulnerable is not None else []


class SnykVulnerability(JsonMappedModel):
    __mapping__ = {
        "id": Attr("_id", str),
        "packageManager": Attr("package_manager", str),
        "packageName": Attr("package_name", str),
        "title": Attr("title", str),
        "publicationTime": Attr("publication_time", str),
        "semver": Attr("semver", SnykSemver),
        "severity": Attr("severity", str),
    }

    def __init__(self, _id: str = None, package_manager: str = None, package_name: str = None,
                 title: str = None, publication_time: str = None, semver: SnykSemver = None, severity: str = None):
        self._id = _id
        self.package_manager = package_manager
        self.package_name = package_name
        self.title = title
        self.publication_time = publication_time
        self.semver = semver
        self.severity = severity

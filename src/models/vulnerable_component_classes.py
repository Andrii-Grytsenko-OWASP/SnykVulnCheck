from alchemize import Attr, JsonMappedModel
from src.models.bom_classes import BomComponent
from src.models.snyk_api_classes import SnykVulnerability


class VulnerableComponent(JsonMappedModel):
    __mapping__ = {
        "type": Attr("component_type", str),
        "bom-ref": Attr("bom_ref", str),
        "publisher": Attr("publisher", str),
        "name": Attr("name", str),
        "version": Attr("version", str),
        "description": Attr("description", str),
        "purl": Attr("purl", str),
        "vulnerabilities": Attr("vulnerabilities", [SnykVulnerability]),
    }

    def __init__(self, component_type: str = None, bom_ref: str = None, publisher: str = None, name: str = None,
                 version: str = None, description: str = None, purl: str = None,
                 vulnerabilities: [SnykVulnerability] = None):
        self.component_type = component_type
        self.bom_ref = bom_ref
        self.publisher = publisher
        self.name = name
        self.version = version
        self.description = description
        self.purl = purl
        self.vulnerabilities = list(vulnerabilities) if vulnerabilities is not None else []

    def copy_from(self, component: BomComponent = None, vulnerabilities: [SnykVulnerability] = None):
        component_is_not_none = component is not None
        self.component_type = component.component_type if component_is_not_none else None
        self.bom_ref = component.bom_ref if component_is_not_none else None
        self.publisher = component.publisher if component_is_not_none else None
        self.name = component.name if component_is_not_none else None
        self.version = component.version if component_is_not_none else None
        self.description = component.description if component_is_not_none else None
        self.purl = component.purl if component_is_not_none else None
        self.vulnerabilities = list(vulnerabilities) if vulnerabilities is not None else []


class VulnerableComponents(JsonMappedModel):
    __mapping__ = {
        "vulnerableComponents": Attr("vulnerable_components", [VulnerableComponent]),
    }

    def __init__(self, vulnerable_components: [VulnerableComponent] = None):
        self.vulnerable_components = list(vulnerable_components) \
            if vulnerable_components is not None else []

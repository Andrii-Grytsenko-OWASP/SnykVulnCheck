from alchemize import Attr, JsonMappedModel


class BomDependency(JsonMappedModel):
    __mapping__ = {
        "ref": Attr("ref", str),
        "dependsOn": Attr("depends_on", [str]),
    }

    def __init__(self, ref: str = None, depends_on: [str] = None):
        self.ref = ref
        self.depends_on = list(depends_on) if depends_on is not None else depends_on


class BomComponent(JsonMappedModel):
    __mapping__ = {
        "type": Attr("component_type", str),
        "bom-ref": Attr("bom_ref", str),
        "publisher": Attr("publisher", str),
        "name": Attr("name", str),
        "version": Attr("version", str),
        "description": Attr("description", str),
        "scope": Attr("scope", str),
        "hashes": Attr("hashes", [object]),
        "licenses": Attr("licenses", [object]),
        "purl": Attr("purl", str),
        "externalReferences": Attr("external_references", [object]),
    }

    def __init__(self, component_type: str = None, bom_ref: str = None, publisher: str = None, name: str = None,
                 version: str = None, description: str = None, scope: str = None, hashes: [object] = None,
                 licenses: [object] = None, purl: str = None, external_references: [object] = None):
        self.component_type = component_type
        self.bom_ref = bom_ref
        self.publisher = publisher
        self.name = name
        self.version = version
        self.description = description
        self.scope = scope
        self.hashes = list(hashes) if hashes is not None else []
        self.licenses = list(licenses) if licenses is not None else []
        self.purl = purl
        self.external_references = list(external_references) \
            if external_references is not None else []


class Bom(JsonMappedModel):
    __mapping__ = {
        "bomFormat": Attr("bom_format", str),
        "specVersion": Attr("spec_version", str),
        "serialNumber": Attr("serial_number", str),
        "version": Attr("version", str),
        "metadata": Attr("metadata", object),
        "components": Attr("components", [BomComponent]),
        "dependencies": Attr("dependencies", [BomDependency]),
    }

    def __init__(self, bom_format: str = None, spec_version: str = None,
                 serial_number: str = None, version: str = None, metadata: object = None,
                 components: [BomComponent] = None, dependencies: [BomDependency] = None):
        self.bom_format = bom_format
        self.spec_version = spec_version
        self.serial_number = serial_number
        self.version = version
        self.metadata = metadata
        self.components = list(components) if components is not None else []
        self.dependencies = list(dependencies) if dependencies is not None else []

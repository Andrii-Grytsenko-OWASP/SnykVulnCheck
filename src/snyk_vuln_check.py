from alchemize import JsonTransmuter

from src.config import CFG
from src.helpers.utils import get_file_data, write_data, in_between
from src.http_client.snyk_api import API
from src.models.bom_classes import Bom, BomComponent
from src.models.snyk_api_response import SnykApiResponse
from src.models.vulnerable_component_classes import VulnerableComponent, VulnerableComponents


class SnykVulnCheck:
    def __init__(self, argv):
        self.bom = None
        self.argv = argv
        self.api = API
        self.vc = VulnerableComponents()

    def run(self):
        if self.check_arguments():
            self.read_bom_file()
            for component in self.bom.components:
                self.check_vulnerability(component)
            self.save_vulnerable_components()
        else:
            self.show_help()

    def check_arguments(self):
        return len(self.argv) == 3

    def read_bom_file(self):
        bom_file_name = CFG.DATA_IN_FOLDER + self.argv[1]
        try:
            self.bom = JsonTransmuter.transmute_from(get_file_data(bom_file_name), Bom)
        except:
            self.bom = Bom()
            self.bom.components = []
            self.bom.dependencies = []

    def save_vulnerable_components(self):
        try:
            result_file_name = CFG.DATA_OUT_FOLDER + self.argv[2]
            write_data(result_file_name, JsonTransmuter.transmute_to(self.vc))
        except:
            self.show_help()

    def check_vulnerability(self, component: BomComponent):
        response = self.api.get_vulnerabilities(component.name)
        if response.code == 200:
            snyk_response = JsonTransmuter.transmute_from(response.data, SnykApiResponse)
            vuln_list = []
            for vulnerability in snyk_response.vulnerabilities:
                if in_between(component.version, vulnerability.semver.vulnerable):
                    vuln_list.append(vulnerability)
            if len(vuln_list) > 0:
                vulnerable_component = VulnerableComponent()
                vulnerable_component.copy_from(component, vuln_list)
                self.vc.vulnerable_components.append(vulnerable_component)

    @staticmethod
    def show_help():
        print(f"Snyk Vulnerability Checking tool\n"
              f"How to use:\n"
              f"python main.py bom.json vulnerable.components.json")

import sys
from src.snyk_vuln_check import SnykVulnCheck


def main(argv):
    application = SnykVulnCheck(argv)
    application.run()


if __name__ == '__main__':
    main(sys.argv)

# Snyk Vulnerabiliy Checking tool
**SnykVulnCheck** - Snyk Vulnerability Checking tool<br>
Tool for checking components from SBOM.json file (Software Bill of Material) against known vulnerabilities by using public API to Snyk Vulnerability DB (https://security.snyk.io/api)
Tool is designed for running inside docker container or as an ordinary python script

**Running in docker**
1. Create docker image by running docker_build.cmd script
2. Run docker image as container by running docker_run.cmd script

By default, folders data_in and data_out will be mapped into the container<br>

**Running as a python script**
1. Install required components by running<br>pip3 install -r requirements.txt
2. Run the script by command<br>python main.py bom-file-name.json vulnerable-components.json

bom-file-name.json should be placed into the data_in folder
vulnerable-components.json result file will be available in the data_out folder

**NOTE**
Edit the DATA_IN_FOLDER and DATA_OUT_FOLDER parameters in src\config.py file if you are running tool as python script on Windows platform.
By default, that parameters are configured for running script in docker container

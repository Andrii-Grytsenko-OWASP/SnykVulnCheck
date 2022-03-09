SET PRJ_HOME=%cd%
docker run --name snyk-vuln-check-container -v %PRJ_HOME%\data_in:/app/data_in -v %PRJ_HOME%\data_out:/app/data_out --rm snyk-vuln-check
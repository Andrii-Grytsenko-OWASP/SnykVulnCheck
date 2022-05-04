class Configuration:
    # https://security.snyk.io/api/listing?q=System.Text.Encodings.Web
    # https://security.snyk.io/api/listing?search=System.Text.Encodings.Web
    SNYK_API_URL = 'https://security.snyk.io/api/'
    SNYK_API_ENDPOINT = 'listing'
    SNYK_API_PARAM = 'search'
    DATA_IN_FOLDER = "/app/data_in/"
    DATA_OUT_FOLDER = "/app/data_out/"


CFG = Configuration()

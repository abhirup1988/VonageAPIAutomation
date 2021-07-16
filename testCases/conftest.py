import pytest
import requests
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

logger = LogGen.loggen()

@pytest.fixture()
def create_session():
    logger.info("Create Session")
    api_request = requests.session()
    api_request.headers.update({"accept": "application/json",
                             "Authorization": ReadConfig.getJWTToken(),
                             "Content-Type": "application/json"})
    return api_request
import json
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
logger = LogGen.loggen()

class conversations:
    def __init__(self,server,api_request):
        self.server = server
        self.api_request = api_request

    def create_conversation(self, payload_path, testdata=None):
        """Takes Payload Path as param from Testfile and Creates a conversation"""
        logger.info("Creating Conversation...")
        api_url = self.server + 'conversations'
        with open('..' +payload_path) as file:
            payload = json.load(file)
        if testdata is not None:
            payload.update(testdata)
        response = self.api_request.post(api_url, json=payload)
        logger.info(response.text)
        return response

    def delete_conversation(self,conversation_id):
        """Takes delete_conversation as param and delete that conversation"""
        logger.info("Deleting Conversation...")
        api_url = self.server + 'conversations/' + conversation_id
        logger.info(api_url)
        response = self.api_request.delete(api_url)
        logger.info(response.text)
        return response

    def create_user(self, payload_path, testdata=None):
        logger.info("Creating User...")
        api_url = self.server + '/users'
        with open('..'+payload_path) as file:
            payload = json.load(file)
        if testdata is not None:
            payload.update(testdata)
        response = self.api_request.post(api_url, json=payload)
        logger.info(response.text)
        return response

    def delete_user(self,userid):
        logger.info('Deleting User....')
        api_url = self.server + '/users/' + userid
        response = self.api_request.delete(api_url)
        logger.info(response.text)
        return response

    def create_member(self,conversation_id, payload_path, testdata=None):
        logger.info('Creating Member....')
        api_url = self.server + f'conversations/{conversation_id}/members'
        logger.info(api_url)
        with open('..' + payload_path) as file:
            payload = json.load(file)
        if testdata is not None:
            payload.update(testdata)
        logger.info(payload)
        response = self.api_request.post(api_url, json=payload)
        logger.info(response.text)
        return response

if __name__ == '__main__':
    con = conversations(ReadConfig.getserver(),ReadConfig.getserver())
    #con.create_conversation()
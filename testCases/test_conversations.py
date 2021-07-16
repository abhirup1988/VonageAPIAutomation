import json
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
from api.conversations import conversations

logger = LogGen.loggen()
server = ReadConfig.getserver()

class Test_001_conversation:
    def test_create_and_delete_conversations(self, create_session):
        logger.info(f"Starting Test_001_conversation::test_create_and_delete_conversations********")
        payload_path = '\\testCases\\json\\create_conversation.json'
        conver = conversations(server=server, api_request=create_session)
        testdata = {"name": "abhiuser1_chat", "display_name": "abhiuser1_chat"}
        cc_response = conver.create_conversation(payload_path, testdata=testdata)
        assert cc_response.status_code == 200
        assert cc_response.json()['id']
        delete_resp = conver.delete_conversation(conversation_id=cc_response.json()['id'])
        assert delete_resp.status_code == 200

    def test_create_duplicate_conversations(self, create_session):
        logger.info("Starting Test_001_conversation::test_create_duplicate_conversations********")
        payload_path = '\\testCases\\json\\create_conversation.json'
        conver = conversations(server=server, api_request=create_session)
        testdata = {"name": "abhiuser1_chat", "display_name": "abhiuser1_chat"}
        conver_response = conver.create_conversation(payload_path, testdata=testdata)
        assert conver_response.status_code == 200
        assert conver_response.json()['id']
        conversation_id = conver_response.json()['id']
        conver_response = conver.create_conversation(payload_path, testdata=testdata)
        assert conver_response.status_code == 400
        assert conver_response.json()['description'] == "The request failed because the conversation name already exists. Please provide a unique conversation name and try again."
        delete_resp = conver.delete_conversation(conversation_id=conversation_id)
        assert delete_resp.status_code == 200

class Test_002_createuser:
    def test_createuser(self, create_session):
        payload_path = '\\testCases\\json\\create_user.json'
        conver = conversations(server=server, api_request=create_session)
        test_data = {"name": "abhiuser1","display_name": "abhiuser1"}
        cu_response = conver.create_user(payload_path=payload_path,testdata=test_data)
        assert cu_response.status_code == 200
        assert cu_response.json()['id']
        user_id = cu_response.json()['id']
        conver.delete_user(userid=user_id)

class Test_003_createmember:
    def test_createmember(self, create_session):
        logger.info(f"Starting Test_003_createmember::test_createmember********")
        self.api_request = create_session
        logger.info("Create Conversation****************")
        payload_path = '\\testCases\\json\\create_conversation.json'
        conver = conversations(server=server, api_request=self.api_request)
        testdata = {"name": "abhiuser2_chat", "display_name": "abhiuser2_chat"}
        cc_response = conver.create_conversation(payload_path, testdata=testdata)
        assert cc_response.status_code == 200
        self.conversation_id = cc_response.json()['id']

        logger.info("Create User****************")
        payload_path = '\\testCases\\json\\create_user.json'
        conver = conversations(server=server, api_request=self.api_request)
        test_data = {"name": "abhiuser2", "display_name": "newfpuser2"}
        cu_response = conver.create_user(payload_path=payload_path, testdata=test_data)
        assert cu_response.status_code == 200
        assert cu_response.json()['id']
        self.user_id = cu_response.json()['id']

        logger.info("Create Member****************")
        payload_path = '\\testCases\\json\\create_member.json'
        conver = conversations(server=server, api_request=self.api_request)
        testdata = {"user_id": self.user_id, "member_id": "MEM-5e84b90a-d6b2-48a1-b382-bcaec7652d56", "member_id_inviting": "MEM-5e84b90a-d6b2-48a1-b382-bcaec7652d56"}
        conversation_id = 'CON-ed64c1fd-a474-46a1-bc5f-7e97df06bd40'
        cm_response = conver.create_member(conversation_id=conversation_id, payload_path=payload_path, testdata=testdata)
        assert cm_response.status_code == 200

    def teardown_method(self):
        logger.info("Delete ****************")
        conver = conversations(server=server, api_request=self.api_request)
        conver.delete_conversation(conversation_id=self.conversation_id)
        conver.delete_user(userid=self.user_id)
# VonageAPIAutomation
`Steps to Run the Project:`
1. pip install -r requirements.txt
2. cd testCases
3. Command(To execute the Framework): `pytest --html=..\\Results\\report.html test_conversations.py`

Note: Configurations\config.ini(To configure the Bearer Token) 

# Reports and Logs:
1. Open the file Results\\report.html(Created in the Project directory) to view Logs and Reports. This will also generate Failure Logs and Reports.
2. I have also committed my Test Result. You can directly view it.

# Feedback
1. Using Vonage API, I am not able to Create Member. So I have put that into Failure Testcase.
2. In order to create a Member we would need to contact the Developer to understand more about the Payload Parameters for keys such as member_id, leg_id etc. I would need more time to understand it.
3. It would take more time to actually debug the issue, hence commited whatever I build in a span of 3 hours.
4. I have focused more on the structure of Automation Framework and make it easy to plug and play for new testcases.

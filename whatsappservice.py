import requests
import json

def SendMessageWhatsapp(data):
    try:
        token = "EAAUQM1QonnkBOwQiPxCcZBf2v2Te60aQolgRMnrAGq1mYWlmbL2nAolXhkHsYTOWCGoZB5nMZB4pNJjy9g0UqLXZCT3nKhaZACdNaZARXZCf2j7Pa69ARx0kKucYa1u0JxEb3P2lnI1ayK9hSkh4vpuZBsUlsHxbg9CpNXXZAPRZBG9rC0YjyDIiPuA5giWc2ZBhhXveCpvpZCaZBm5DvjIp48NnKBHCujx4ogAdeaOLrDd8ZD"
        api_url = "https://graph.facebook.com/v17.0/114784988391901/messages"
        headers = {"Content-Type": "application/json", "Authorization": "Bearer " + token}
        response = requests.post(api_url, data = json.dumps(data), headers = headers)
        if response.status_code == 200:
            return True
        
        return False
    except Exception as exception:
        print(exception)
        return False
import requests
import json

def SendMessageWhatsapp(data):
    try:
        token = "EAAUQM1QonnkBO5mIZB6fuJxBtgkBfFwIMjyZC24FY6MXR2aRCHDu5vIklr1Hz0moEeBZAcGDySBeUL2duPDIoRNYtXzi8reXpRymj4u0KjLsEhxPBFu2ufOIo3XnvKvxmvgvpyzJSHU5s2dTCuV8bHkhQNlgShEk6LOzZA5dlsVp3heRLTGGD7m10SYsgWDizdk7yPWJt2dzPZBobAiP9"
        api_url = "https://graph.facebook.com/v17.0/114784988391901/messages"
        headers = {"Content-Type": "application/json", "Authorization": "Bearer " + token}
        response = requests.post(api_url, data = json.dumps(data), headers = headers)
        if response.status_code == 200:
            return True
        
        return False
    except Exception as exception:
        print(exception)
        return False
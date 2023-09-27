import requests
import json

def SendMessageWhatsapp(data):
    try:
        token = "EAAUQM1QonnkBOy8MCE6hNart3Ix0OMlftN9ZBjyoKTjUZCmWXxzMqMs4PpE68m1AkpVVA4g9m6PcSzPZAzQmajujLMec7qCVNA8nMhc5beGd4QcJJD3vd3PoSKXscWWI4q7qpFkkeJs9q6BzM60xgZAshxsk4IiWqbVMD476lHrO5CL2z6cHjny3SdtaPDk0lYvO"
        api_url = "https://graph.facebook.com/v17.0/114784988391901/messages"
        headers = {"Content-Type": "application/json", "Authorization": "Bearer " + token}
        response = requests.post(api_url, data = json.dumps(data), headers = headers)
        if response.status_code == 200:
            return True
        
        return False
    except Exception as exception:
        print(exception)
        return False
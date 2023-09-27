from flask import Flask, request
import util
import whatsappservice

app = Flask(__name__)

# Replace this with your actual access token
ACCESS_TOKEN = "QN32NBU9V2MMO0Ssw73jgv93NC"

@app.route('/welcome', methods=['GET'])
def index():
    return "Welcome developer"

@app.route('/whatsapp', methods=['GET'])
def verify_token():
    try:
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")
        
        if token is not None and token == ACCESS_TOKEN:
            return challenge
        else:
            return "Invalid token", 400
    except Exception as e:
        print(f"Error in verify_token: {str(e)}")
        return "Error", 400

@app.route('/whatsapp', methods=['POST'])
def received_message():

    try:
        body = request.get_json()
        entry = (body["entry"])[0]
        changes = (entry["changes"])[0]
        value = changes["value"]
        message = (value["messages"])[0]
        number = message["from"]


        text = util.GetTextUser(message)
        GenerateMessage(text, number)
        print(text)


        return "EVENT_RECEIVED"
    except:    
        return "EVENT_RECEIVED"


def GenerateMessage(text, number):
    
    if "text" in text:
        data = util.TextMessage("Text", number)
    if "format" in text:
        data = util.TextFormatMessage(number)
    if "image" in text:
        data = util.ImageMessage(number)
    if "video" in text:
        data = util.VideoMessage(number)        
    if "audio" in text:
        data = util.AudioMessage(number)
    if "document" in text:
        data = util.DocumentMessage(number)
    if "location" in text:
        data = util.LocationMessage(number)
    if "button" in text:
        data = util.ButtonsMessage(number)
    if "list" in text:
        data = util.ListMessage(number)

    whatsappservice.SendMessageWhatsapp(data)

if __name__ == "__main__":
    app.run()



def GetTextUser(message):
    text = ""
    typeMessage = message["type"]

    if typeMessage == "text":
        text = (message["text"])["body"]
    elif typeMessage == "interactive":
        interactiveObject = message["interactive"]
        typeInteractive = interactiveObject["type"]
        if typeInteractive == "button_reply":
            text = (interactiveObject["button_reply"])["title"]
        elif typeInteractive == "list_reply":
            text = (interactiveObject["list_reply"])["title"]
        else: 
            print("sin mensaje")

    else:
        print ("sin mensaje")

    return text

def TextMessage(text, number):
    data = {
            "messaging_product": "whatsapp",    
            "to": number,
            "text": {
                "body": text
            },
            "type": "text",
            }
    return data 

def TextFormatMessage(number):
    data = {
            "messaging_product": "whatsapp",    
            "to": number,
            "type": "text",
            "text": {
                "body": "*hola* \n _me llamo_ \n ~franco~"
            }
            }
    return data 


def ImageMessage(number):
    data = {
            "messaging_product": "whatsapp",    
            "to": number,
            "type": "image",
            "image": {
                "link": "https://fazhostel.com/wp-content/uploads/2022/09/Faz_S1_F-55-1024x659.jpg"
            }
            }
    return data 

def AudioMessage(number):
    data = {
            "messaging_product": "whatsapp",    
            "to": number,
            "type": "audio",
            "audio": {
                "link": ""
            }
            }
    return data 

def VideoMessage(number):
    data = {
            "messaging_product": "whatsapp",    
            "to": number,
            "type": "video",
            "video": {
                "link": ""
            }
            }
    return data 

def DocumentMessage(number):
    data = {
            "messaging_product": "whatsapp",    
            "to": number,
            "type": "document",
            "document": {
                "link": ""
            }
            }
    return data 


def LocationMessage(number):
    data = {
                "messaging_product": "whatsapp",   
                "recipient_type": "individual",
                "to": number,
                "type": "location",
                "location": {
                    "latitude": "-31.39935655381755",
                    "longitude": "-64.17991327865026",
                    "name": "Faz Hostel",
                    "address": "General Paz 1539, X5000 Cordoba",
                }
            }
    return data 

def ButtonsMessage(number):
    data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": number,
            "type": "interactive",
            "interactive": {
                "type": "button",
                "body": {
                    "text": "Ya estas registrado/a?"
                },
                "action": {
                    "buttons": [
                        {
                            "type": "reply",
                            "reply": {
                                "id": "001",
                                "title": "🤖 Registrarse 🤖"
                            }
                        },
                        {
                            "type": "reply",
                            "reply": {
                                "id": "002",
                                "title": "👉 Iniciar Sesion 👈"
                            }
                        }
                    ]
                }
            }
        }
    return data 


def ListMessage(number):
    data = {
    "messaging_product": "whatsapp",
    "to": number,
    "type": "interactive",
    "interactive": {
        "type": "list",
        "body": {
            "text": "✅ I have these options"
        },
        "footer": {
            "text": "Select an option"
        },
        "action": {
            "button": "See options",
            "sections": [
                {
                    "title": "Buy and sell products",
                    "rows": [
                        {
                            "id": "main-buy",
                            "title": "Buy",
                            "description": "Buy the best product your home"
                        },
                        {
                            "id": "main-sell",
                            "title": "Sell",
                            "description": "Sell your products"
                        }
                    ]
                },
                {
                    "title": "📍center of attention",
                    "rows": [
                        {
                            "id": "main-agency",
                            "title": "Agency",
                            "description": "Your can visit our agency"
                        },
                        {
                            "id": "main-contact",
                            "title": "Contact center",
                            "description": "One of our agents will assist you"
                        }
                    ]
                }
            ]
        }
    }
}
    return data 


import json
import apiai
import urllib.request
import pprint
from urllib.parse import quote_plus

CLIENT_ACCESS_TOKEN = '3a79f257e43e497b9d07d18c51e7497d'

def botResponseReciever(queryMessage):
    ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

    request = ai.text_request()

    request.query = queryMessage

    response = request.getresponse()

    rawData = str(response.read())
    rawData = rawData.replace(r"\n" , "")       #Remove \n 
    rawData = rawData.replace(r"b'" , "" , 1)   #Remove b'
    rawData = rawData.replace(r"\'" , "")   #Remove \' which causes prob in the bot message
    jsonData = rawData[0:-1]                        #Remove ' in the end

    data = json.loads(jsonData)
    #pprint.pprint(data)
    send_data = (
        data['result']['fulfillment']['speech'],
        data['result']['metadata']['intentName']
    )
    return send_data
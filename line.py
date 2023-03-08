import requests
import json

def sendReplyMessageTextLine(tokenLine, replyToken, message):
    url = "https://api.line.me/v2/bot/message/reply"

    payload = json.dumps({
    "replyToken": replyToken,
    "messages": [
        {
            "type": "text",
            "text": message
        }
    ]
    })
    headers = {
    'Authorization': 'Bearer '+tokenLine,
    'Content-Type': 'application/json'
    }

    response = requests.post(url, headers=headers, data=payload)
    return response


def sendReplyFlexMessageLine(tokenLine, replyToken, message):
    url = "https://api.line.me/v2/bot/message/reply"

    payload = json.dumps({
    "replyToken": replyToken,
    "messages": [
        {
        "type": "flex",
        "altText": "เลือกประเภท",
        "contents": message
        }
    ]
    })
    headers = {
    'Authorization': 'Bearer '+tokenLine,
    'Content-Type': 'application/json'
    }

    response = requests.post(url, headers=headers, data=payload)
    return response

def sendReplyFlexMessageAllMsgLine(tokenLine, replyToken, message):
    url = "https://api.line.me/v2/bot/message/reply"

    payload = json.dumps({
    "replyToken": replyToken,
    "messages": [
        {
            "type": "text",
            "text": message['msg']
        },
        {
        "type": "flex",
        "altText": "เลือกประเภท",
        "contents": message['flex']
        }
    ]
    })
    headers = {
    'Authorization': 'Bearer '+tokenLine,
    'Content-Type': 'application/json'
    }

    response = requests.post(url, headers=headers, data=payload)
    return response

def sendReplyStickerMessageAllMsgLine(tokenLine, replyToken, message, packageId, stId):
    url = "https://api.line.me/v2/bot/message/reply"

    payload = json.dumps({
    "replyToken": replyToken,
    "messages": [
        {
            "type": "text",
            "text": message
        },
        {
            "type": "sticker",
            "packageId": packageId,
            "stickerId": stId
        }
    ]
    })
    headers = {
    'Authorization': 'Bearer '+tokenLine,
    'Content-Type': 'application/json'
    }

    response = requests.post(url, headers=headers, data=payload)
    return response
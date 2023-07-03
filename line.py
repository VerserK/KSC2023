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

    response = requests.request("POST", url, headers=headers, data=payload)
    return response


def sendReplyFlexMessageLine(tokenLine, replyToken, message, alt):
    url = "https://api.line.me/v2/bot/message/reply"

    payload = json.dumps({
    "replyToken": replyToken,
    "messages": [
        {
        "type": "flex",
        "altText": alt,
        "contents": message
        }
    ]
    })
    headers = {
    'Authorization': 'Bearer '+tokenLine,
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
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

    response = requests.request("POST", url, headers=headers, data=payload)
    return response

def sendReplyStickerMessageAllMsgLine(tokenLine, replyToken, message, packageId, stId, lastFlex):
    url = "https://api.line.me/v2/bot/message/reply"
    
    if lastFlex == 'ไม่มีข้อมูล' :
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
    else :
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
            },
            {
                "type": "flex",
                "altText": "promotion",
                "contents": lastFlex
            }
        ]
        })
    headers = {
    'Authorization': 'Bearer '+tokenLine,
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response

def sendReplyFlexListMessageLine(tokenLine, replyToken, list1, list2, alt):
    url = "https://api.line.me/v2/bot/message/reply"
    
    if list2 == [] :
        payload = json.dumps({
            "replyToken": replyToken,
            "messages": [
                {
                    "type": "flex",
                    "altText": alt,
                    "contents": {
                        "type": "carousel",
                        "contents": list1
                    }
                }
            ]
        })
    else :
        payload = json.dumps({
            "replyToken": replyToken,
            "messages": [
                {
                    "type": "flex",
                    "altText": alt,
                    "contents": {
                        "type": "carousel",
                        "contents": list1
                    }
                },
                {
                    "type": "flex",
                    "altText": alt,
                    "contents": {
                        "type": "carousel",
                        "contents": list2
                    }
                }
            ]
        })
    headers = {
    'Authorization': 'Bearer '+tokenLine,
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response

def sendReplyImageMessageAllMsgLine(tokenLine, replyToken, message, image):
    url = "https://api.line.me/v2/bot/message/reply"

    payload = json.dumps({
    "replyToken": replyToken,
    "messages": [
        {
            "type": "text",
            "text": message
        },
        {
            "type": "image",
            "originalContentUrl": image,
            "previewImageUrl": image
        }
    ]
    })
    headers = {
    'Authorization': 'Bearer '+tokenLine,
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response